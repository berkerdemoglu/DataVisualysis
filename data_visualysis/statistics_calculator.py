import statistics_functions as sf


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
		return sf.find_mean(self.dataset)

	def median(self):
		"""Return the median of the dataset."""
		return sf.find_median(self.dataset)

	def mode(self, mode_occurrence="no"):
		"""Return the mode of the dataset."""
		return sf.find_mode(self.dataset, mode_occurrence)

	def std(self):
		"""Return the standard deviation of the dataset."""
		return sf.find_standard_deviation(self.dataset)

	def var(self):
		"""Return the variance of the dataset."""
		return sf.find_variance(self.dataset)

	def percentile(self, percentile):
		return sf.find_percentile(self.dataset, percentile)

	def occurrences(self):
		return sf.find_occurrences(self.dataset)