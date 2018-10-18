import unittest

from merger import open_file, get_full_name, get_first_last_name


class TestApp(unittest.TestCase):

	def test_sanity(self):
		self.assertEqual(True, True)

	def test_get_full_name_type(self):
		self.assertEqual(list, type(get_full_name(open_file())))

	def test_get_first_last_name_type(self):
		self.assertEqual(list, type(get_first_last_name(open_file())))
