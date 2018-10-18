import json
import requests
from demjson import decode

def open_file():
	with open('ms_data_sample.json') as f:
		return json.load(f)


def get_full_name(f):
	l = list()
	for i in list(f.keys()):
		l.append(f[i]['fullName'])
	return l


def get_first_last_name(l):
	nl = list()
	for i in l:
		names = i.split()
		first = names[0]
		last = names[len(names) - 1]
		nl.append(tuple([first, last]))
	return nl


def lookup_npi(l):
	for i in l:
		url = 'https://npiregistry.cms.hhs.gov/api?first_name={}&last_name={}&pretty=true'\
			.format(i[0], i[1])
		res = requests.get(url)
		print(res.json()['results'][0]['number'])
		# print(res.json().find('number'))
		# if 'number' in res.json():
		# 	print()
		# res_json = decode(res.json())
		# print(res_json)

	return 'foo'


provider_names = get_full_name(open_file())
provider_names_discrete = get_first_last_name(provider_names)
npi = lookup_npi(provider_names_discrete)
