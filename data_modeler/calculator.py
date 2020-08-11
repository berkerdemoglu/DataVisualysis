import machinelearning_functions as mpl

class Calculator():
	"""
	A class that calculates values such as median,
	mode etc. Used for data analysis.
	"""


	def __init__(self, dataset):
		"""Initialize a calculator object."""
		self.dataset = dataset

	def use_recent_dataset(self, dataset):
		"""Use the most recent dataset."""
		self.dataset = dataset

	def see_dataset(self):
		"""
		Asks the user if they wish to see the whole dataset or not 
		if the dataset is larger than 30 elements.
		If user inputs 'y', the whole dataset is printed. If user inputs 'n',
		"""
		if len(self.dataset) > 30:
			prompt = "Would you like to see the whole dataset? It is "
			prompt += str(len(self.dataset)) + " elements long.\n"
			prompt += "(Enter 'y' to see the whole dataset, 'n' to see a part of the dataset.)\n"
			while True:
				user_choice = input(prompt)
				if user_choice == 'y':
					print(self.dataset)
					break
				elif user_choice == 'n':
					print(self.dataset[0:9], "...", self.dataset[-10:])
					break
				else: # if invalid input:
					print("You have entered an invalid value. Please try again.")
		else:
			print(self.dataset)

	def create_offline_dataset(self):
		"""Create a default dataset using the random module."""
		return mpl.create_dataset()

	def mean(self):
		"""Return the mean of the dataset."""
		return mpl.find_mean(self.dataset)

	def median(self):
		"""Return the median of the dataset."""
		return mpl.find_median(self.dataset)

	def mode(self, mode_occurrence="no"):
		"""Return the mode of the dataset."""
		return mpl.find_mode(self.dataset, mode_occurrence)

	def std(self):
		"""Return the standard deviation of the dataset."""
		return mpl.find_standard_deviation(self.dataset)

	def var(self):
		"""Return the variance of the dataset."""
		return mpl.find_variance(self.dataset)

	def percentile(self, percentile):
		return mpl.find_percentile(self.dataset, percentile)