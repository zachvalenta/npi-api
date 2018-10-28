import json
import requests


def open_file():
	with open('ms_data_sample.json') as f:
		return json.load(f)


def get_full_name(f):
	full_names = dict()
	for i in list(f.keys()):
		full_names[i] = f[i]['fullName']
	return full_names


def get_first_last_name(d):
	first_last_names = dict()
	for i in d.items():
		key = i[0]
		first, *rest, last = i[1].split()
		first_last_names[key] = tuple([first, last])
	return first_last_names


def lookup_npi(l):
	nl = list()
	for i in l:
		url = 'https://npiregistry.cms.hhs.gov/api?first_name={}&last_name={}&pretty=true'\
			.format(i[0], i[1])
		res = requests.get(url)
		# be nice to fix formatting via demjson
		nl.append(res.json()['results'][0]['number'])

	return nl


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
npi = lookup_npi(provider_names_first_last)
add_npi(npi)
