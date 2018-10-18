import json


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
		nl.append(set([first, last]))
	print(type(nl))
	return nl


provider_names = get_full_name(open_file())
get_first_last_name(provider_names)
