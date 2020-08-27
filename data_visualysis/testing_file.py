import unittest
import json
import numpy as np
import time
from scipy import stats
from statistics_calculator import StatisticsCalculator
from data_visualysis import DataVisualysis


################################
######## DATAVISUALYSIS ########
################################


class TestDataVisualysis(unittest.TestCase):
	"""Tests for the DataVisualysis class."""

	def setUp(self):
		"""Create a DataVisualysis object for use in all test methods."""
		self.dataset = [2, 1, 2, 3, 5, 1, 2, 4]
		self.data_modeler = DataVisualysis(dataset=self.dataset)
		self.file = 'json_files/testcases.json'


	# REGULAR METHODS
	def test_init(self):
		"""Test that __init__() works correctly."""
		pass


	def test_grd(self):
		"""Test that generate_random_dataset() works correctly."""
		pass


	def test_gord(self):
		"""Test that generate_offline_random_dataset() works correctly."""
		pass


	def test_usedataset(self):
		"""Test that use_dataset() works correctly."""
		pass


	def test_saving(self):
		"""Test that save_current_dataset() works correctly."""
		pass


	def test_showdataset(self):
		"""Test that show_dataset() works correctly."""
		pass


	def test_showresults(self):
		"""Test that show_results() works correctly."""
		pass


	def test_retoccur(self):
		"""Test that return_occurrences() works correctly."""
		pass



	# STATIC METHODS
	def test_filecount(self):
		"""Test that set_file_count() works correctly."""
		self.data_modeler.set_file_count(0, self.file)

		with open(self.file, 'r') as f_obj:
			file_count = json.load(f_obj)

		self.assertEqual(file_count, 0)


	def test_storeapikey(self):
		"""Test that store_api_key() works correctly."""
		self.data_modeler.store_api_key('lol', self.file)

		with open(self.file, 'r') as f_obj:
			stored_key = json.load(f_obj)

		self.assertEqual(stored_key, 'lol')


	def test_loadapikey(self):
		"""Test that load_api_key() works correctly."""
		stored_key = self.data_modeler.load_api_key(self.file)

		with open(self.file, 'r') as f_obj:
			read_key = json.load(f_obj)

		self.assertEqual(read_key, stored_key)


	def test_comparison(self):
		"""Test that compare_datasets() works correctly."""
		# Empty, compare_datasets() has not been coded yet.
		pass


################################
##### STATISTICSCALCULATOR #####
################################


class TestStatisticsCalculator(unittest.TestCase):
	"""Tests for the StatisticsCalculator class."""

	def setUp(self):
		"""Create a StatisticsCalculator object for use in all test methods."""
		self.sample = [2, 1, 2, 3, 5, 1, 2, 4]
		self.calculate = StatisticsCalculator(self.sample)


	def test_mean(self):
		"""Tests that mean() works correctly."""
		my_mean = self.calculate.mean()
		real_mean = np.mean(self.sample)

		self.assertEqual(my_mean, real_mean)


	def test_median(self):
		"""Tests that median() works correctly."""
		my_median = self.calculate.median()
		real_median = np.median(self.sample)

		self.assertEqual(my_median, real_median)


	def test_mode(self):
		"""Tests that mode() works correctly."""
		my_mode = self.calculate.mode()
		mode_obj = stats.mode(self.sample)
		real_mode = mode_obj.mode[0]

		self.assertEqual(my_mode, real_mode)


	def test_std(self):
		"""Tests that std() works correctly."""
		my_std = self.calculate.std()
		real_std = np.std(self.sample)

		self.assertEqual(my_std, real_std)


	def test_var(self):
		"""Tests that var() works correctly."""
		my_var = self.calculate.var()
		real_var = np.var(self.sample)

		self.assertEqual(my_var, real_var)


	def test_percentile(self):
		"""Tests that percentile() works correctly."""
		my_result = self.calculate.percentile(75)
		real_result = np.percentile(self.sample, 75)

		self.assertEqual(my_result, real_result)
		

	def test_percentile_2(self):
		"""Tests that percentile() works correctly."""
		my_result_2 = self.calculate.percentile(25)
		real_result_2 = np.percentile(self.sample, 25)

		self.assertEqual(my_result_2, real_result_2)
		

	def test_occurrences(self):
		"""Tests that percentile() works correctly."""
		pass


###################################
######### CODE TIME TESTING #######
###################################


def calc_code_time(filename, times, func, *args):
	"""Test the speed of a code snippet. Import a file and run a function.
	The results will be stored in a directory you specify."""
	# Print arguments.
	print("Testing the function:", func)
	print("With the arguments:", args)
	print("Saving results to:", filename)
	# Calculate execution time of the function.
	exec_times = []
	for i in range(times):
		start_time = time.time()
		func(*args)
		exec_times.append(float("{}".format((time.time() - start_time))))

	# Save results in the provided filename.
	with open(filename, 'w') as f_obj:
		json.dump(exec_times, f_obj)


dv = DataVisualysis(path='saved_files/seeds.json')
calc_code_time('saved_files/codetimes.json', 10000, np.mean, dv.dataset)


###################################
########## RUN UNITTESTS ##########
###################################
print("\n\n")
unittest.main()