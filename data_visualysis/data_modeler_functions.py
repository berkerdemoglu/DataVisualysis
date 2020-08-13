import requests
import json
import random
from math import floor, fmod
from data_modeler_exceptions import *

def chdef_dir(path):
	"""Used in change_default_directory()"""
	with open('json_files/default_directory.json', 'w') as f_obj:
		json.dump(path, f_obj)

	if path == 'json_files/numbers_data.json':
		print("You have not provided a path for the default directory. The presumed directory,", path, "will be used.")
	else:
		print("Default directory changed to", path + ".")


def loaddef_dir():
	"""Used in some functions to load the default directory."""
	with open('json_files/default_directory.json', 'r') as f_obj:
		stored_path = json.load(f_obj)

	# If stored path is not a string, raise an error.
	if not isinstance(stored_path, str):
		raise InvalidPathError
	return stored_path


def init_datavisualysis(filepath, dataset):
	"""Used in __init__"""
	if not dataset and not filepath: # if neither dataset nor filepath was not provided:
		filename = loaddef_dir()
		with open(filename, 'r') as file:
			dataset = json.load(file)
		msg = "You have provided neither a data set or a file path. \nThe dataset in the "
		msg += "default directory, {}, will be used.".format(filename)
		print(msg, "(You can change the dataset later).\n")
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
	return dataset


def create_dataset_random_module(mini, maxi, numbers, ntype):
	"""Used in create_offline_random_dataset"""
	if ntype == 'float':
		dataset = [random.uniform(mini,maxi) for i in range(1,numbers+1)]
		msg = "You have generated a new dataset of floating point numbers using the random module."
	elif ntype == 'int':
		dataset = [random.randint(mini,maxi) for i in range(1,numbers+1)]
		msg = "You have generated a new dataset of integers using the random module."
	else:
		raise NTypeError(ntype)

	default_dir = loaddef_dir()
	with open(default_dir, 'w') as file:
		json.dump(dataset, file)
	print(msg, "The dataset will be stored in the default directory.")
	return dataset


def datasetfromrandom_org(numbers, mini, maxi, replacement, api_key):
	"""Get numbers from random.org."""
	url = 'https://api.random.org/json-rpc/1/invoke'
	data = {
	    "jsonrpc": "2.0",
	    "method": "generateIntegers",
	    "params": {
        "apiKey": api_key,
	    "n": numbers,
		"min": mini,
		"max": maxi,
		"replacement": replacement
		},
		"id": 42
		}
	params = json.dumps(data)
	response = requests.post(url, params)
	
	# If invalid inputs have been provided for grn():
	if 'error' in response.text:
		with open('json_files/request_random.json', 'w') as f_obj:
			json.dump(response.text, f_obj)
		raise RandomOrgError
	# Store the request in a .json file.
	with open('json_files/request_random.json', 'w') as f_obj:
		json.dump(response.text, f_obj)

	# Store the generated numbers in a .json file list format with integer elements.
	data_index = response.text.index("data")
	completion_index = response.text.index("completion")
	stored_data = response.text[data_index + 6:completion_index - 2]
	listified_data = stored_data.strip('[]').replace('"', '').replace(' ', '').split(',')
	dataset = [int(n) for n in listified_data]
	return dataset


def generate_random_numbers(numbers, mini, maxi, replacement, api_key):
	"""Get a new random number list using random.org and save it in 
	the default directory."""
	# If numbers are greater than 10000, random.org will generate an error.
	# A workaround is to divide the numbers into groups.
	# Eg: numbers=54321, floored=5, remainder=4321, 5 for loops.
	dataset = []
	if numbers > 10000:
		floored = floor(numbers)
		remainder = fmod(numbers, 10000)
		for i in range(0, floored):
			# Add 10000 numbers in each iteration.
			dataset.extend(datasetfromrandom_org(10000, mini, maxi, replacement, api_key))
		dataset.extend(datasetfromrandom_org(remainder, mini, maxi, replacement, api_key))
	else:
		dataset = datasetfromrandom_org(numbers, mini, maxi, replacement, api_key)

	# Store the dataset in the default directory.
	default_dir = loaddef_dir()
	with open(default_dir, 'w') as file:
		json.dump(dataset, file)

	# Print a message to inform the user that a new dataset was generated and return the dataset.
	msg = "You have generated a new dataset using random.org."
	print(msg, "It will be stored in the default directory.")
	return dataset


def reset_count(count):
	"""Used in set_file_count()"""
	if not isinstance(count, int):
		# if count is not an integer, raise an exception.
		raise CountNotIntegerError(count)

	with open('json_files/file_count.json', 'w') as f_obj:
		f_obj.write(str(count))
	print("Reset the file count in json_files/file_count.json to", str(count) + ".")


def use_specfdir(path):
	"""Used in use_specific_dataset()"""
	with open(path, 'r') as file:
		dataset = json.load(file)
	print("You are now using the dataset stored in {}".format(path) + ".")
	return dataset


def save_dataset(path, dataset):
	"""Used in save_current_dataset"""
	if not path:
		with open('json_files/file_count.json', 'r') as f_obj:
			current_count = f_obj.read()
			save_file = 'saved_files/dataset_{}'.format(current_count) + '.json'

		with open('json_files/file_count.json', 'w') as f_obj:
			f_obj.write(str(int(current_count) + 1))

		with open(save_file, 'w') as f_obj:
			json.dump(dataset, f_obj)
		print("Saved the file in {}".format(save_file) + ".")

	# Else, save the file in the provided directory.
	else:
		with open(path, 'w') as f_obj:
			json.dump(dataset, f_obj)
		print("Saved the file in {}".format(path) + ".")


def print_dataset(dataset):
	"""Used in show_dataset()"""
	if len(dataset) > 30:
		prompt = "Would you like to see the whole dataset? It is "
		prompt += str(len(dataset)) + " elements long.\n"
		prompt += "(Enter 'y' to see the whole dataset, 'n' to see a part of the dataset.)\n"
		while True:
			user_choice = input(prompt)
			if user_choice == 'y':
				print(dataset)
				break
			elif user_choice == 'n':
				print(dataset[0:9], "...", dataset[-10:])
				break
			else: # if invalid input:
				print("You have entered an invalid value. Please try again.")
	else:
		print("The dataset is {} elements long.\n".format(len(dataset)))
		print(dataset)


def print_some_results(dataset, mode_var):
	"""Used in show_results()"""
	# If the dataset has more than 50 elements, do not print the dataset.
	if len(dataset) < 50:
		print("Dataset:", dataset)
	else:
		print("The dataset was omitted because it was too large.")
	# Print other analytics.
	print("Maximum Value in the Dataset:", max(dataset))
	print("Minimum Value in the Dataset:", min(dataset))
	print("Sum of Values in the Dataset:", sum(dataset))

	# Print the mode of the dataset.
	if isinstance(mode_var, list):
		print("Mode:", str(mode_var[0]) + ", Occurrences:", mode_var[1])
	else:
		print("Mode:", mode_var)