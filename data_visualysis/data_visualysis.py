from statistics_calculator import StatisticsCalculator
import data_visualysis_functions as dvf

"""If this file is being imported, print a message to the terminal, 
specifying the version of DataVisualysis."""
if __name__ != '__main__':
	print("© DataVisualysis 0.2.1\n")


class DataModeler:
	"""A class for data visualization and analysis.
	The main class of DataVisualysis."""

	# DUNDER METHODS
	def __init__(self, path=None, dataset=None):
		"""
		Initialize the data modeler object. A data set or a file path 
		(.json file) containing a data set can be specified. 
		If both the data set and the file path were provided, the file path
		will be used for dataset.

		@param path: The path of the file containing the data set.
		@param dataset: The dataset itself.
		"""
		self.dataset = dvf.init_dataset(path, dataset)
		self.calculate = StatisticsCalculator(self.dataset)
		if path:
			self.path = path
		else:
			self.path = 'No path provided'

	def __repr__(self):
		"""Return the string representation of this object. Fallback method."""
		return dvf.reprstr_method(self.dataset, self.path)

	def __str__(self):
		"""Return the string representation of this object. 
		Called when printing the object to the terminal."""
		return dvf.reprstr_method(self.dataset, self.path)


	# REGULAR METHODS
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

	def show_results(self, mode_occurrence=False):
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

	def return_occurrences(self, mode_include=False):
		"""
		Prints how many times each value appears in the list.

		@param mode_include: Takes 'true' or 'false' values.
		"""
		if mode_include:
			mode_var = self.calculate.mode(True)
			if mode_var == 'The list has no mode.':
				print(mode_var)
			else:
				print("Mode:", str(mode_var[0]) + ", Occurrences:", mode_var[1])
		elif not mode_include:
			pass
		else:
			dvf.raise_mode_include_error(mode_include)

		return self.calculate.occurrences()

	def compare_datasets(self, dataset1, dataset2=None):
		"""
		Compares two given datasets.

		@param dataset1: The first dataset
		@param dataset2: The second dataset
		@param mode_occurrence: Include how many times the mode of the dataset occurs or not
		"""
		# Create a copy of the original dataset.
		original_dataset = self.dataset[:]

		# If a second dataset was not provided, use self.dataset instead.
		if not dataset2:
			dataset2 = self.dataset

		# Print the results for dataset1.
		self.calculate.dataset = dataset1
		mode_var = self.calculate.mode(True)
		mean = self.calculate.mean()
		q1 = self.calculate.percentile(25)
		median = self.calculate.median()
		q3 = self.calculate.percentile(75)
		std = self.calculate.std()
		variance = self.calculate.var()
		sum_1, max_1, min_1 = sum(dataset1), max(dataset1), min(dataset1)
		print("Showing results for the first dataset:\n")
		dvf.print_statistics(sum_1, max_1, min_1, mean, q1, median, q3, std, variance)

		# Print the results for dataset2.
		self.calculate.dataset = dataset2
		mode_var_2 = self.calculate.mode(True)
		mean_2 = self.calculate.mean()
		q1_2 = self.calculate.percentile(25)
		median_2 = self.calculate.median()
		q3_2 = self.calculate.percentile(75)
		std_2 = self.calculate.std()
		variance_2 = self.calculate.var()
		sum_2, max_2, min_2 = sum(dataset2), max(dataset2), min(dataset2)
		print("\nShowing results for the second dataset:\n")
		dvf.print_statistics(sum_2, max_2, min_2, mean_2, q1_2, median_2, q3_2, std_2, variance_2)

		# Print the differences of statistics of the two datasets.
		print("\nDifferences of statistics:\n")
		print("Difference of Maximum Values:", abs(max_1 - max_2))
		print("Difference of Minimum Values:", abs(min_1 - min_2))
		print("Difference of Sum of Values:", abs(sum_1 - sum_2))
		print("Difference of Means:", abs(mean - mean_2))
		print("Difference of Medians:", abs(median - median_2))
		print("Difference of Standard Deviations:", abs(std - std_2))
		print("Difference of Variances:", abs(variance - variance_2))

		# Set self.dataset back to its original.
		self.dataset = original_dataset

	# STATIC METHODS
	@staticmethod
	def set_file_count(count=0, path="json_files/file_count.json"):
		"""
		Sets the file count in json_files/file_count.json.

		@param count: The file count to be stored in json_files/file_count.json
		"""
		dvf.reset_count(count, path)

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

		@param path: The path of the file containing the API key.
		"""
		return dvf.return_api_key(path)

	@staticmethod
	def show_colormaps():
		"""Prints every available colormap."""
		dvf.print_colormaps()

	@staticmethod
	def dataset_from_path(path):
		"""
		Reads a .json file containing an array of numbers.

		@param path: The path of the .json file
		"""
		return dvf.load_json_dataset(path)

	@staticmethod
	def store_dataset_in_path(dataset, path):
		"""
		Stores a given dataset in a .json file.

		@param path: The path of the .json file
		"""
		dvf.store_json_dataset(dataset, path)

	# GRAPH METHODS
	def scatter_dataset(self, dataset2=None, colormap='viridis', 
		title="Dataset", save=False, path=None, bbox_inches='tight'):
		"""Scatters the values in the dataset and 
		plots the graph using matplotlib."""
		dvf.plot_scatter(self.dataset, dataset2, colormap, title, save, path, bbox_inches)

	def line_graph(self, dataset2=None, title="Dataset", save=False, 
		path=None, bbox_inches='tight'):
		"""Draws a line graph connecting the values 
		in the dataset using matplotlib."""
		dvf.draw_line_graph(self.dataset, dataset2, title, save, path, bbox_inches)
