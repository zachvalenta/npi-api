import unittest

from merger import load_original_json, parse_provider_names, get_first_last_name


class TestApp(unittest.TestCase):

	def test_sanity(self):
		self.assertEqual(True, True)

	def test_get_full_name_type(self):
		self.assertEqual(list, type(parse_provider_names(load_original_json())))

	def test_get_first_last_name_type(self):
		self.assertEqual(list, type(get_first_last_name(load_original_json())))
