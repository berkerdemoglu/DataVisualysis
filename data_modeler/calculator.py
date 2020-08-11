import machine_learning_functions as mlf

class Calculator():
	"""
	A class that calculates values such as median,
	mode etc. Used for data analysis. Also contains
	some functions for data_modeler.py.
	"""


	def __init__(self, dataset):
		"""Initialize a calculator object."""
		self.dataset = dataset

	def use_recent_dataset(self, dataset):
		"""Use the most recent dataset."""
		self.dataset = dataset
		
	def create_offline_dataset(self):
		"""Create a default dataset using the random module."""
		return mlf.create_dataset()

	def mean(self):
		"""Return the mean of the dataset."""
		return mlf.find_mean(self.dataset)

	def median(self):
		"""Return the median of the dataset."""
		return mlf.find_median(self.dataset)

	def mode(self, mode_occurrence="no"):
		"""Return the mode of the dataset."""
		return mlf.find_mode(self.dataset, mode_occurrence)

	def std(self):
		"""Return the standard deviation of the dataset."""
		return mlf.find_standard_deviation(self.dataset)

	def var(self):
		"""Return the variance of the dataset."""
		return mlf.find_variance(self.dataset)

	def percentile(self, percentile):
		return mlf.find_percentile(self.dataset, percentile)