from calculator import Calculator
import data_modeler_functions as dmf
import json

"""If this file is being imported, print a message to the console, 
specifying the version of DataVisualysis."""
if __name__ != '__main__':
	print("© DataVisualysis 0.1.1\n")

class DataVisualysis():
	"""A class for data visualization and analysis.
	The main class of the program - DataVisualysis."""

	def __init__(self, filepath=None, dataset=None):
		"""
		Initialize the data modeler object. A data set or a file path 
		(.json file) containing a data set can be specified. 
		If both the data set and the file path were provided, the file path
		will be used for dataset.

		@param filepath: The path of the file containing the data set
		@param dataset: The dataset itself
		"""
		self.dataset = dmf.init_dataset(filepath, dataset)
		self.calculate = Calculator(self.dataset)

	# Regular Methods
	def generate_random_dataset(self, numbers=100, mini=0, 
		maxi=100, replacement="true"):
		"""
		Create a random number dataset of integers using random.org and 
		set self.dataset to the newly created dataset and save the dataset
		in json_files/numbers_data.json.

		@param numbers: How many numbers (integers) to generate
		@param mini: The lower limit (integer)
		@param maxi: The upper limit (integer)
		@param replacement: "true" or "false". Create a dataset with reoccuring numbers or not.
		"""

		# Call get_random_numbers to get random numbers (grn stands for get_random_numbers).
		# Set self.dataset to the generated numbers in list format.
		self.dataset = dmf.grn(numbers, mini, maxi, replacement)
		self.calculate.dataset = self.dataset

	def generate_offline_random_dataset(self, mini=0, 
		maxi=100, numbers=100, ntype="int"):
		"""
		DEFAULT-Sets self.dataset to a 100-element list, 
		generated using the random module. The list contains floating 
		point numbers in the 0-100 range.

		@param mini: The lower limit
		@param maxi: The upper limit
		@param numbers: How many numbers to generate
		@param ntype: The type of numbers you want to generate - "int" or "float"
		"""
		self.dataset = dmf.create_dataset_random_module(mini, maxi, numbers, ntype)
		self.calculate.dataset = self.dataset

	def use_specific_dataset(self, path='json_files/numbers_data.json'):
		"""
		Changes the dataset to a dataset from a specified .json file. 
		The file must contain an array of numbers. If a file path was not provided,
		the dataset in json_files/numbers_data.json will be used.

		@param path: The path of the .json file containing the dataset
		"""
		self.dataset = dmf.use_specfdir(path)
		self.calculate.dataset = self.dataset

	def save_current_dataset(self, path=None):
		"""
		If a path is not provided, saves the current dataset to another file. 
		The file will be named dataset_(file_count).json, located in the json_files folder. 
		'file_count.json' will be incremented every time a dataset is saved in the default directory.
		If a path is provided, the file will be saved in the provided path with the provided name.

		@param path: The path of the file to be saved
		"""
		# If a path was not provided, save the file in the default directory.
		dmf.save_dataset(path, self.dataset)

	def show_dataset(self):
		"""
		Asks the user if they wish to see the whole dataset or not 
		if the dataset is larger than 30 elements.
		If user inputs 'y', the whole dataset is printed. If user inputs 'n',
		"""
		dmf.print_dataset(self.dataset)

	def show_results(self, mode_occurrence="no"):
		"""
		Prints every data analysis result.

		@param mode_occurrence: Include how many times the mode of the dataset occurs or not
		"""
		mode_var = self.calculate.mode(mode_occurrence)
		dmf.print_some_results(self.dataset, mode_var)
		print("Mean:", self.calculate.mean())
		print("Median:", self.calculate.median())
		print("Standard Deviation:", self.calculate.std())
		print("Variance:", self.calculate.var())

	# Static and Class Methods
	@staticmethod
	def set_file_count(count=0):
		"""
		Sets the file count in json_files/file_count.json.

		@param count: The file count to be stored in json_files/file_count.json
		"""
		dmf.reset_count(count)