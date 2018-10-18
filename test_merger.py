import unittest

from merger import get_full_name, open_file


class TestApp(unittest.TestCase):

	def test_sanity(self):
		self.assertEqual(True, True)

	def test_get_names(self):
		self.assertEqual(list, type(get_full_name(open_file())))
