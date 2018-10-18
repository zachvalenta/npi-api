import json


def open_file():
	with open('ms_data_sample.json') as f:
		return json.load(f)


def get_full_name(f):
	l = list()
	for i in list(f.keys()):
		l.append(f[i]['fullName'])
	return l


def do_something(s):
	print(s)


provider_names = get_full_name(open_file())
do_something(provider_names)
