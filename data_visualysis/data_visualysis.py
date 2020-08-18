from statistics_calculator import StatisticsCalculator
import data_visualysis_functions as dvf

"""If this file is being imported, print a message to the terminal, 
specifying the version of DataVisualysis."""
if __name__ != '__main__':
	print("© DataVisualysis 0.1.3.2\n")


class DataVisualysis:
	"""A class for data visualization and analysis.
	The main class of DataVisualysis."""

	def __init__(self, path=None, dataset=None):
		"""
		Initialize the data modeler object. A data set or a file path 
		(.json file) containing a data set can be specified. 
		If both the data set and the file path were provided, the file path
		will be used for dataset.

		@param path: The path of the file containing the data set.
		@param dataset: The dataset itself.
		"""
		self.dataset = dvf.init_datavisualysis(path, dataset)
		self.calculate = StatisticsCalculator(self.dataset)

	# Regular Methods
	def generate_random_dataset(self, api_key, numbers=100, mini=0, 
		maxi=100, replacement="true", method="store"):
		"""
		Create a random number dataset of integers using random.org and 
		set self.dataset to the newly created dataset and save the dataset
		in json_files/numbers_data.json.

		@param numbers: How many numbers (integers) to generate
		@param mini: The lower limit (integer)
		@param maxi: The upper limit (integer)
		@param replacement: "true" or "false". Create a dataset with reoccuring numbers or not.
		@param method: Takes 'return' or 'store' values. 'return' returns a 
		dataset generated using random.org. 'store' overwrites the numbers_data.json
		file inside json_files and sets the object's dataset to the new dataset.
		"""

		# Call get_random_numbers to get random numbers (grn stands for get_random_numbers).
		# Set self.dataset to the generated numbers in list format.
		if method == 'return':
			return dvf.generate_random_numbers(numbers, mini, maxi, replacement,
			 api_key, method)

		elif method == 'store':
			self.dataset = dvf.generate_random_numbers(numbers, mini, maxi, replacement,
			 api_key, method)
			self.calculate.dataset = self.dataset

		else:
			dvf.raise_method_error(method)

	def generate_offline_random_dataset(self, mini=0, 
		maxi=100, numbers=100, ntype="int", method="store"):
		"""
		DEFAULT-Sets self.dataset to a 100-element list, 
		generated using the random module. The list contains floating 
		point numbers in the 0-100 range.

		@param mini: The lower limit
		@param maxi: The upper limit
		@param numbers: How many numbers to generate
		@param ntype: The type of numbers you want to generate - "int" or "float"
		@param method: Takes 'return' or 'store' values. 'return' returns a 
		dataset generated using the random module. 'store' overwrites the numbers_data.json
		file inside json_files and sets the object's dataset to the new dataset.
		"""
		if method == 'return':
			return dvf.create_dataset_random_module(mini, maxi, numbers, ntype, method)
		elif method == 'store':
			self.dataset = dvf.create_dataset_random_module(mini, maxi, numbers, ntype)
			self.calculate.dataset = self.dataset
		else:
			dvf.raise_method_error(method)

	def use_dataset(self, path='json_files/numbers_data.json'):
		"""
		Changes the dataset to a dataset from a specified .json file. 
		The file must contain an array of numbers. If a file path was not provided,
		the dataset in json_files/numbers_data.json will be used.

		@param path: The path of the .json file containing the dataset.
		"""
		self.dataset = dvf.use_specfdir(path)
		self.calculate.dataset = self.dataset

	def save_current_dataset(self, path=None):
		"""
		If a path is not provided, saves the current dataset to another file. 
		The file will be named dataset_(file_count).json, located in the json_files
		folder. 'file_count.json' will be incremented every time a dataset is saved in the 
		default directory. If a path is provided, the file will be saved in the provided 
		path with the provided name.

		@param path: The path of the file to be saved
		"""
		# If a path was not provided, save the file in the default directory.
		dvf.save_dataset(path, self.dataset)

	def show_dataset(self):
		"""
		Asks the user if they wish to see the whole dataset or not 
		if the dataset is larger than 30 elements.
		If user inputs 'y', the whole dataset is printed. If user inputs 'n',
		"""
		dvf.print_dataset(self.dataset)

	def show_results(self, mode_occurrence="no"):
		"""
		Prints every data analysis result.

		@param mode_occurrence: Include how many times the mode of the dataset occurs or not
		"""
		mode_var = self.calculate.mode(mode_occurrence)
		dvf.print_some_results(self.dataset, mode_var)
		print("Mean:", self.calculate.mean())
		print("1st Quartile:", self.calculate.percentile(25))
		print("Median (2nd Quartile):", self.calculate.median())
		print("3rd Quartile:", self.calculate.percentile(75))
		print("Standard Deviation:", self.calculate.std())
		print("Variance:", self.calculate.var())

	def return_occurrences(self, mode_include='false'):
		"""
		Prints how many times each value appears in the list.

		@param mode_include: Takes 'true' or 'false' values.
		"""
		if mode_include == 'true':
			mode_var = self.calculate.mode('yes')
			if mode_var == 'The list has no mode.':
				print(mode_var)
			else:
				print("Mode:", str(mode_var[0]) + ", Occurrences:", mode_var[1])

		elif mode_include == 'false':
			pass
		else:
			dvf.raise_mode_include_error(mode_include)
		return self.calculate.occurrences()

	# Static and Class Methods
	@staticmethod
	def set_file_count(count=0):
		"""
		Sets the file count in json_files/file_count.json.

		@param count: The file count to be stored in json_files/file_count.json
		"""
		dvf.reset_count(count)

	@staticmethod
	def change_default_directory(path='json_files/numbers_data.json'):
		"""
		Changes the default directory of the class.

		@param path: The path of the file to be used as the default directory.
		Default option for the path is json_files/numbers_data.json.
		"""
		dvf.chdef_dir(path)

	@staticmethod
	def store_api_key(api_key, path="json_files/api_key.json"):
		"""
		Stores the api key in a file.

		@param api_key: The api key to be stored.
		@param path: The path to the .json file to store the key in.
		"""
		dvf.write_api_key(api_key, path)

	@staticmethod
	def load_api_key(path="json_files/api_key.json"):
		"""
		Returns the stored API key.

		@param path: The path of the file that contains the API key.
		"""
		return dvf.return_api_key(path)

	@staticmethod
	def compare_datasets(dataset1, dataset2):
		"""
		Compares two given datasets.

		@param dataset1: The first dataset
		@param dataset2: The second dataset
		"""
		# NOT IMPLEMENTED YET!
		pass