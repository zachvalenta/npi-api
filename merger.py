import json
import requests


def load_original_json():
	with open('ms_data_sample.json') as f:
		return json.load(f)


def parse_provider_names(json):
	names = dict()  # TODO: modify in place instead of new dict
	for i in list(json.keys()):
		first, *rest, last = json[i]['fullName'].split()
		names[i] = tuple([first, last])
	return names


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
	# TODO: cache NPI
	return plus_npi


# def add_npi(d):
# 	orig = get_original_json()
# 	for i in list(orig):
#
# 		orig[i]['npi_number'] = d[orig[i]]
#
#
#
# 	f = open_file()
# 	tmp = 0
# 	for i in list(f):
# 		f[i]['npi_number'] = d[tmp]
# 		tmp += 1
# 	new_file = open('ms_data_merged.json', 'w')
# 	new_file.write(json.dumps(f))
# 	new_file.close()


provider_names = parse_provider_names(load_original_json())
import pdb; pdb.set_trace()
key_to_npi = lookup_npi(provider_names)
# add_npi(key_to_npi)
