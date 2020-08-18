import unittest
import json
from data_visualysis import DataVisualysis

"""
Currently incomplete. Will be used to test the functions of data_visualysis.py
"""

class TestDataVisualysis(unittest.TestCase):
	"""Tests for the class DataVisualysis."""

	data_modeler = DataVisualysis()

	# REGULAR METHODS
	def test_init(self):
		"""Test that __init__() works correctly."""
		d_obj = TestDataVisualysis.data_modeler
		pass


	def test_grd(self):
		"""Test that generate_random_dataset() works correctly."""
		d_obj = TestDataVisualysis.data_modeler
		pass


	def test_gord(self):
		"""Test that generate_offline_random_dataset() works correctly."""
		d_obj = TestDataVisualysis.data_modeler
		pass


	def test_usedataset(self):
		"""Test that use_dataset() works correctly."""
		d_obj = TestDataVisualysis.data_modeler
		pass


	def test_saving(self):
		"""Test that save_current_dataset() works correctly."""
		d_obj = TestDataVisualysis.data_modeler
		pass


	def test_showdataset(self):
		"""Test that show_dataset() works correctly."""
		d_obj = TestDataVisualysis.data_modeler
		pass


	def test_showresults(self):
		"""Test that show_results() works correctly."""
		d_obj = TestDataVisualysis.data_modeler
		pass


	def test_occurrences(self):
		"""Test that return_occurrences() works correctly."""
		d_obj = TestDataVisualysis.data_modeler
		pass


	# STATIC METHODS
	def test_filecount(self):
		"""Test that set_file_count() works correctly."""
		d_obj = TestDataVisualysis.data_modeler
		d_obj.set_file_count(5)

		with open('json_files/file_count.json', 'r') as f_obj:
			file_count = json.load(f_obj)

		self.assertEqual(file_count, 5)


	def test_storeapikey(self):
		"""Test that store_api_key() works correctly."""
		d_obj = TestDataVisualysis.data_modeler
		pass


	def test_loadapikey(self):
		"""Test that load_api_key() works correctly."""
		d_obj = TestDataVisualysis.data_modeler
		pass


	def test_comparison(self):
		"""Test that compare_datasets() works correctly."""
		d_obj = TestDataVisualysis.data_modeler
		pass


###################################
unittest.main()
###################################