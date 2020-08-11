from calculator import Calculator
from generate_numbers import get_random_numbers as grn
import json

class DataModeler():
	"""A class to deal with measurements."""


	def __init__(self, dataset=None):
		"""Initialize the data modeler object."""
		if not dataset: # if dataset was not provided:
			filename = 'json_files/numbers_data.json'
			with open(filename, 'r') as file:
				loaded_file = (json.load(file)).strip('[]').replace('"', '').replace(' ', '').split(',')
				dataset = [int(n) for n in loaded_file]
		self.dataset = dataset
		self.calculate = Calculator(dataset)

	def create_random_number_dataset(self, numbers=100, mini=0, maxi=100, 
		replacement="true", method="generateIntegers"):
		"""
		Create a random number dataset using random.org and 
		set self.dataset to the newly created dataset.
		"""
		filename = 'json_files/numbers_data.json'
		# Call get_random_numbers to get random numbers.
		grn(numbers, mini, maxi, replacement, method)
		# Load the file and set self.dataset to the generated numbers in list format.
		with open(filename, 'r') as file:
			loaded_file = (json.load(file)).strip('[]').replace('"', '').replace(' ', '').split(',')
			self.dataset = [int(n) for n in loaded_file]
			self.calculate.use_recent_dataset(self.dataset)
		print("You have generated a new dataset.")

	def create_offline_number_dataset(self):
		"""
		Sets self.dataset to a 100-element list, 
		generated using the random module. The list contains floating 
		point numbers in the 0-100 range.
		"""
		self.dataset = self.calculate.create_offline_dataset()
		self.calculate.use_recent_dataset(self.dataset)
		print("You have generated a new dataset.")

	def print_dataset(self):
		"""Prints the dataset on the terminal."""
		self.calculate.see_dataset()

	def print_results(self, mode_occurrence="no"):
		"""Prints every data analysis result."""
		# If the dataset has more than 50 elements, do not print the dataset.
		if len(self.dataset) < 50:
			if self.dataset == [1, 2, 3, 4, 5]:
				print("You are using the default dataset: [1, 2, 3, 4, 5].")
			else:
				print("List: ", self.dataset)
		else:
			print("The dataset was omitted because it was too large.")
		# Print other analytics.
		print("Mean:", self.calculate.mean())
		print("Median:", self.calculate.median())
		mode_var = self.calculate.mode(mode_occurrence)
		if isinstance(mode_var, list):
			print("Mode:", str(mode_var[0]) + ", Occurrences:", mode_var[1], "times")
		else:
			print("Mode:", mode_var)
		print("Standard Deviation:", self.calculate.std())
		print("Variance:", self.calculate.var())