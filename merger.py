import json


def open_file():
	with open('ms_data_sample.json') as f:
		return json.load(f)


def read(f):
	for i in list(f.keys()):
		print(f[i]['fullName'])


read(open_file())
