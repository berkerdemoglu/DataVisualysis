from statistics_functions import find_mode, find_occurrences
import numpy as np


class StatisticsCalculator:
	"""
	A class that calculates values such as median,
	mode etc. Used for data analysis. Also contains
	some functions for data_modeler.py.
	"""


	def __init__(self, dataset):
		"""Initialize a calculator object."""
		self.dataset = dataset

	def mean(self):
		"""Return the mean of the dataset."""
		return np.mean(self.dataset)

	def median(self):
		"""Return the median of the dataset."""
		return np.median(self.dataset)

	def mode(self, mode_occurrence=False):
		"""Return the mode of the dataset."""
		return find_mode(self.dataset, mode_occurrence)

	def std(self):
		"""Return the standard deviation of the dataset."""
		return np.std(self.dataset)

	def var(self):
		"""Return the variance of the dataset."""
		return np.var(self.dataset)

	def percentile(self, percentile):
		"""Return the percentile of the dataset."""
		return np.percentile(self.dataset, percentile)

	def occurrences(self):
		"""Return the number of occurrences of each number in the dataset."""
		return find_occurrences(self.dataset)


######### TESTING #########

if __name__ == "__main__":
	sc = StatisticsCalculator([1, 2, 2, 4, 5, 2, 4])
	a1 = sc.mean()
	a2 = sc.median()
	a3 = sc.mode()
	a4 = sc.std()
	a5 = sc.var()
	a6 = sc.percentile(75)
	a7 = sc.occurrences()
	print(a1, a2, a3, a4, a5, a6, a7)