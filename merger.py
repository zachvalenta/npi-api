import json
import requests


def open_file():
	with open('ms_data_sample.json') as f:
		return json.load(f)


def get_full_name(f):
	plus_whole_name = dict()  # instead of creating a new dict, modify in place?
	for i in list(f.keys()):
		plus_whole_name[i] = f[i]['fullName']
	return plus_whole_name


def get_first_last_name(d):
	plus_first_last_name = dict()
	for i in d.items():
		key = i[0]
		first, *rest, last = i[1].split()
		plus_first_last_name[key] = tuple([first, last])
	return plus_first_last_name


def lookup_npi(d):
	plus_npi = dict()
	for i in d.items():
		url = 'https://npiregistry.cms.hhs.gov/api?first_name={}&last_name={}&pretty=true'\
			.format(i[1][0], i[1][1])
		res = requests.get(url)
		try:
			npi = res.json()['results'][0]['number']
			plus_npi[i[0]] = npi
		except IndexError:
			print('NPI lookup failed for {}'.format(i))
			plus_npi[i[0]] = ''
	return plus_npi


def add_npi(l):
	f = open_file()
	tmp = 0
	for i in list(f):
		f[i]['npi_number'] = l[tmp]
		tmp += 1
	new_file = open('ms_data_merged.json', 'w')
	new_file.write(json.dumps(f))
	new_file.close()


provider_names_full = get_full_name(open_file())
provider_names_first_last = get_first_last_name(provider_names_full)
key_to_npi = lookup_npi(provider_names_first_last)
add_npi(key_to_npi)
