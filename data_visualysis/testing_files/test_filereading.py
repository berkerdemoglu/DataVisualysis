import unittest

class FileTestCase(unittest.TestCase):
	"""Tests for files."""
	def test_empty_file(self):
		"""Does an empty file return None?"""
		with open('empty_file.json', 'r') as f_obj:
			contents = f_obj.read()
		self.assertEqual(contents, "")


unittest.main()