from calculator import Calculator
from generate_numbers import get_random_numbers as grn
import json

"""If this file is being run in another Python file,
print a friendly message to the console."""
if __name__ != '__main__':
	print("DataVisualysis 0.1.0\n")

class DataModeler():
	"""A class for data visualization and data analysis."""


	def __init__(self, dataset=None, filepath=None):
		"""
		Initialize the data modeler object. A data set or a file path 
		(.json file) containing a data set can be specified. 
		If both the data set and the file path were provided, the file path
		will be used for dataset.
		"""
		if not dataset and not filepath: # if neither dataset nor filepath was not provided:
			filename = 'json_files/numbers_data.json'
			with open(filename, 'r') as file:
				dataset = json.load(file)
			msg = "You have not provided a dataset. The default dataset will be used."
			print(msg, "(You can change the dataset later on.)\n")
		elif not dataset and filepath: # if only filepath was provided:
			with open(filepath, 'r') as file:
				dataset = json.load(file)
			print("The dataset you provided in the file will be used.\n")
		elif dataset and not filepath: # if only dataset was provided:
			print("The dataset you provided will be used.\n")
		else: # if dataset and filepath were provided:
			with open(filepath, 'r') as file:
				dataset = json.load(file)
			print("You have provided both the data set and the file path.", 
				"The data set in the file will be used.\n")

		self.dataset = dataset
		self.calculate = Calculator(dataset)

	def generate_random_dataset(self, numbers=100, mini=0, maxi=100, 
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
			self.dataset = json.load(file)
		self.calculate.use_recent_dataset(self.dataset)
		print("You have generated a new dataset using random.org.")

	def generate_offline_dataset(self):
		"""
		Sets self.dataset to a 100-element list, 
		generated using the random module. The list contains floating 
		point numbers in the 0-100 range.
		"""
		self.dataset = self.calculate.create_offline_dataset()
		self.calculate.use_recent_dataset(self.dataset)
		print("You have generated a new dataset using the random module.")

	def use_default_dataset(self):
		"""Uses the default path used during generating 
		random datasets using random.org or the random module."""
		filename = 'json_files/numbers_data.json'
		with open(filename, 'r') as file:
			self.dataset = json.load(file)
		self.calculate.use_recent_dataset(self.dataset)
		print("You are now using the default dataset stored in {}".format(filename) + ".")

	def use_dataset(self, path):
		"""Changes the dataset to a dataset from a specified .json file. 
		The file must contain an array of numbers. A file path must be provided."""
		with open(path, 'r') as file:
			self.dataset = json.load(file)
		self.calculate.use_recent_dataset(self.dataset)
		print("You are now using the dataset stored in {}".format(path) + ".")

	def save_current_dataset(self, path=None):
		"""
		If a path is not provided, saves the current dataset to another file. 
		The file will be named dataset_(file_count).json, located in the json_files folder. 
		'file_count.json' will be incremented every time a dataset is saved in the default directory.
		If a path is provided, the file will be saved in the provided path with the provided name.
		"""
		# If a path was not provided, save the file in the default directory.
		if not path:
			with open('json_files/file_count.json', 'r') as f_obj:
				current_count = f_obj.read()
				save_file = 'json_files/dataset_{}'.format(current_count) + '.json'

			with open('json_files/file_count.json', 'w') as f_obj:
				f_obj.write(str(int(current_count) + 1))

			with open(save_file, 'w') as f_obj:
				json.dump(self.dataset, f_obj)
			print("Saved the file in {}".format(save_file) + ".")


		# Else, save the file in the provided directory.
		else:
			with open(path, 'w') as f_obj:
				json.dump(self.dataset, f_obj)
				print("Saved the file in {}".format(path) + ".")

	def show_dataset(self):
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

	def reset_file_count(self):
		"""Resets the file count in json_files/file_count.json."""
		with open('json_files/file_count.json', 'w') as f_obj:
			f_obj.write(str(0))
		print("Reset the file count in json_files/file_count.json to 0.")

	def print_results(self, mode_occurrence="no"):
		"""Prints every data analysis result."""
		# If the dataset has more than 50 elements, do not print the dataset.
		if len(self.dataset) < 50:
			print("Dataset:", self.dataset)
		else:
			print("The dataset was omitted because it was too large.")
		# Print other analytics.
		print("Maximum Value in the Dataset:", max(self.dataset))
		print("Minimum Value in the Dataset:", min(self.dataset))
		print("Sum of Values in the Dataset:", sum(self.dataset))
		print("Mean:", self.calculate.mean())
		print("Median:", self.calculate.median())
		mode_var = self.calculate.mode(mode_occurrence)
		if isinstance(mode_var, list):
			print("Mode:", str(mode_var[0]) + ", Occurrences:", mode_var[1], "times")
		else:
			print("Mode:", mode_var)
		print("Standard Deviation:", self.calculate.std())
		print("Variance:", self.calculate.var())