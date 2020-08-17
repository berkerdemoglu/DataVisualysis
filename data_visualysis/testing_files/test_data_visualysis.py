"""
Currently incomplete. Will be used to test the functions of data_visualysis.py
"""

import sys
sys.path.append('D:/kodlama/python modules/other projects/python_machine_learning/data_modeler')

import unittest
from data_visualysis import DataVisualysis

class TestDataVisualysis(unittest.TestCase):
	"""Tests for the class DataVisualysis."""

	def test_randomorg(self):
		"""Test that a dataset generated from random.org works correctly."""
		data_modeler = DataVisualysis()
		data_modeler.generate_random_dataset()
		# self.assertEqual() # UNCOMMENT THIS LINE

unittest.main()