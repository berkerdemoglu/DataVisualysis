import json
import random
from math import floor, fmod
from collections import namedtuple

import requests
import matplotlib.pyplot as plt

from data_visualysis_exceptions import *


def return_api_key(path):
	"""Loads the API key from a given file path. 
	The default option is the file, json_files/api_key.json."""
	# Load the API key from the provided file.
	with open(path, 'r') as f_obj:
		api_key = json.load(f_obj)

	return api_key # Return the API key.


def write_api_key(api_key, path):
	"""Writes the API key to a file."""
	# Store the API key in a file.
	with open(path, 'w') as f_obj:
		json.dump(api_key, f_obj)
	# Print a message informing the user of successfully writing the API key.
	print("Stored the provided API key in {}".format(path) + ".")


def chdef_dir(path):
	"""Changes the default directory stored in 
	json_files/default_directory.json."""
	# Dump the provided path to a file.
	with open('json_files/default_directory.json', 'w') as f_obj:
		json.dump(path, f_obj)

	# If a path was not provided, the default directory 
	# will be presumed as json_files/numbers_data.json.
	if path == 'json_files/numbers_data.json':
		msg = "You have not provided a path for the default directory."
		print(msg, "The presumed directory,", path, "will be used.")
	else:
		print("Default directory changed to", path + ".")


def loaddef_dir():
	"""Loads the default directory stored in 
	json_files/default_directory.json and returns it."""
	# Read the stored default directory.
	with open('json_files/default_directory.json', 'r') as f_obj:
		stored_path = json.load(f_obj)

	# If stored path is not a string, raise an error.
	if not isinstance(stored_path, str):
		raise InvalidStoredPathError

	return stored_path # Return the default directory.


def init_dataset(path, dataset):
	"""Helps initialize a DataVisualysis object. Used in the __init__ method."""

	# If neither a dataset nor a path was not provided:
	if not dataset and not path:
		filename = loaddef_dir()
		with open(filename, 'r') as file:
			dataset = json.load(file)
		msg = "You have provided neither a data set or a file path. \nThe datas"
		msg += "et in the default directory, {}, will be used.".format(filename)
		print(msg, "(You can change the dataset later).\n")

	# If only a path was provided:
	elif not dataset and path:
		with open(path, 'r') as f_obj:
			dataset = json.load(f_obj)
		print("The dataset you provided in the file will be used.\n")

	# If only a dataset was provided:
	elif dataset and not path:
		print("The dataset you provided will be used.\n")

	# If a dataset and a path were provided:
	else: 
		with open(path, 'r') as file:
			dataset = json.load(file)
		print("You have provided both the data set and the file path.", 
			"The data set in the file will be used.\n")

	return dataset # Return the dataset.


def create_dataset_random_module(mini, maxi, numbers, ntype, method='store'):
	"""Used in create_offline_random_dataset"""

	# Generates random decimal numbers.
	if ntype == 'float':
		dataset = [random.uniform(mini,maxi) for i in range(1,numbers+1)]
		msg = "You have generated a new dataset of decimal "
		msg += "numbers using the random module."

	# Generates random integers.
	elif ntype == 'int':
		dataset = [random.randint(mini,maxi) for i in range(1,numbers+1)]
		msg = "You have generated a new dataset of integers "
		msg += "using the random module."

	# Raises an error if ntype is not 'float' or 'int'.
	else:
		raise NTypeError(ntype)

	if method == 'store':
		# Store the dataset in the default directory.
		# Load the default directory.
		default_dir = loaddef_dir()
		with open(default_dir, 'w') as file:
			json.dump(dataset, file)
		print(msg, "\nIt will be stored in the default directory.")

	elif method == 'return':
		# Returns the dataset.
		return dataset

	else:
		# Raise an error if method is not 'store' and 'return'.
		raise MethodError(method)


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
	
	# If invalid inputs have been provided:
	if 'error' in response.text:
		# Store the error response in a .json file.
		with open('json_files/randomorg_request.json', 'w') as f_obj:
			json.dump(response.text, f_obj)

		# If the API key does not have enough bits for the operation:
		if 'The operation requires' in response.text:
			raise NotEnoughBitsError

		# If an invalid API key was provided:
		elif "Parameter 'apiKey' is malformed" in response.text:
			raise InvalidAPIKeyError

		# If some other error occurred:
		raise RandomOrgError

	# Store the response in a .json file.
	with open('json_files/randomorg_request.json', 'w') as f_obj:
		json.dump(response.text, f_obj)

	# Store the generated numbers in a .json file list 
	# format with integer elements.
	data_index = response.text.index("data")
	completion_index = response.text.index("completion")
	stringified_data = response.text[data_index + 6:completion_index - 2]
	listified_data = stringified_data.strip('[]').replace('"', '')
	dataset = [int(n) for n in listified_data.replace(' ', '').split(',')]

	return dataset # Return the dataset.


def generate_random_numbers(numbers, mini, maxi, replacement, 
	api_key, method='store'):
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
			dataset.extend(datasetfromrandom_org(10000, mini, maxi, replacement, 
				api_key))
		dataset.extend(datasetfromrandom_org(remainder, mini, maxi, replacement, 
			api_key))
	else:
		dataset = datasetfromrandom_org(numbers, mini, maxi, replacement, 
			api_key)

	# Print a message to inform the user that a new dataset 
	# swas generated and return the dataset.
	msg = "You have generated a new dataset using random.org."
	if method == 'store':
		# Load the default directory.
		default_dir = loaddef_dir()
		# Store the dataset in the default directory.
		with open(default_dir, 'w') as file:
			json.dump(dataset, file)
		print(msg, "\nIt will be stored in the default directory.")

	elif method == 'return':
		# Return the dataset.
		return dataset

	else:
		# Raise an error if method is not 'store' and 'return'.
		raise MethodError


def reset_count(count, path):
	"""Used in set_file_count()"""
	# If count is not an integer, raise an exception.
	if not isinstance(count, int):
		raise CountNotIntegerError(count)

	# Store the provided value in a .json file.
	with open(path, 'w') as f_obj:
		f_obj.write(str(count))
	print("Reset the file count in {} to".format(path), str(count) + ".")


def use_specfdir(path):
	"""Used in use_specific_dataset()"""
	# Load the dataset.
	with open(path, 'r') as file:
		dataset = json.load(file)
	print("You are now using the dataset stored in {}".format(path) + ".")

	return dataset # Return the dataset.


def save_dataset(path, dataset):
	"""Used in save_current_dataset"""
	# If a path for the save was not provided, save the current
	# dataset with the suffix in json_files/file_count.json.
	if not path:
		# Read the count in file_count.json
		with open('json_files/file_count.json', 'r') as f_obj:
			current_count = f_obj.read()
			save_file = 'saved_files/dataset_{}'.format(current_count) + '.json'

		# Increment the file_count by 1.
		with open('json_files/file_count.json', 'w') as f_obj:
			f_obj.write(str(int(current_count) + 1))

		# Write the dataset in the save file.
		with open(save_file, 'w') as f_obj:
			json.dump(dataset, f_obj)

		print("Saved the file in {}".format(save_file) + ".")

	# Else, save the file in the provided directory.
	else:
		# Save the dataset in the provided path.
		with open(path, 'w') as f_obj:
			json.dump(dataset, f_obj)

		print("Saved the file in {}".format(path) + ".")


def load_json_dataset(path):
	"""Used in dataset_from_path()."""
	with open(path, 'r') as f_obj:
		dataset = json.load(f_obj)

	if not isinstance(dataset, list):
		raise StoredDatasetError

	return dataset


def store_json_dataset(dataset, path):
	"""Used in store_dataset()."""
	if not isinstance(dataset, list):
		raise DatasetNotListError

	with open(path, 'w') as f_obj:
		json.dump(dataset, f_obj)


def print_dataset(dataset):
	"""Used in show_dataset()"""
	# If the dataset has more than 30 elements, ask the user
	# if they wish to see the whole dataset.
	if len(dataset) > 30:
		prompt = "Would you like to see the whole dataset? It is "
		prompt += "{} elements long.\n(Enter 'y' to ".format(len(dataset))
		prompt += "see the whole dataset, 'n' to see a part of the dataset.)\n"
		# Create a while loop to accept only valid responses such as 'y' or 'n'.
		while True:
			user_choice = input(prompt)
			# Print the whole dataset.
			if user_choice == 'y':
				print(dataset)
				break

			# Print the first and last 10 elements of the dataset.
			elif user_choice == 'n':
				print(dataset[0:9], "...", dataset[-10:])
				break
			else: # if invalid input:
				print("You have entered an invalid value. Please try again.")

	else:
		# Print the whole dataset.
		print("The dataset is {} elements long.\n".format(len(dataset)))
		print(dataset)


def print_some_results(dataset, mode_var):
	"""Used in show_results()"""
	# If the dataset has more than 50 elements, do not print the dataset.
	print("The dataset has", len(dataset), "elements. ", end="")
	if len(dataset) < 50:
		print("Dataset:", dataset)
	else:
		print("The dataset was omitted because it was too large.")
	# Print other analytics.
	print("Maximum Value in the Dataset:", f"{max(dataset):,}")
	print("Minimum Value in the Dataset:", f"{min(dataset):,}")
	print("Sum of Values in the Dataset:", f"{sum(dataset):,}")

	# Print the mode of the dataset.
	if isinstance(mode_var, list):
		print("Mode:", str(mode_var[0]) + ", Occurrences:", mode_var[1])

	elif mode_var == "The list has no mode.":
		print(mode_var)

	else:
		print("Mode:", mode_var)


def print_statistics(sum_, max_, min_, mean, q1, median, q3, std, variance):
	"""Print given statistics."""
	print("Maximum Value in the Dataset:", max_)
	print("Minimum Value in the Dataset:", min_)
	print("Sum of Values in the Dataset:", sum_)
	print("Mean:", mean)
	print("1st Quartile:", q1)
	print("Median (2nd Quartile):", median)
	print("3rd Quartile:", q3)
	print("Standard Deviation:", std)
	print("Variance:", variance)


def return_cmaps():
	"""Returns a dictionary of matplotlib colormaps."""
	cmaps = {
		'viridis': plt.cm.viridis,'plasma': plt.cm.plasma,
		'inferno': plt.cm.inferno,'magma': plt.cm.magma,
		'cividis': plt.cm.cividis,'Greys': plt.cm.Greys,
		'Purples': plt.cm.Purples,'Blues': plt.cm.Blues,'Greens': plt.cm.Greens,
		'Oranges': plt.cm.Oranges,'Reds': plt.cm.Reds,'YlOrBr': plt.cm.YlOrBr,
		'YlOrRd': plt.cm.YlOrRd,'OrRd': plt.cm.OrRd,'PuRd': plt.cm.PuRd,
		'RdPu': plt.cm.RdPu,'BuPu': plt.cm.BuPu,'GnBu': plt.cm.GnBu,
		'PuBu': plt.cm.PuBu,'YlGnBu': plt.cm.YlGnBu,'PuBuGn': plt.cm.PuBuGn,
		'BuGn': plt.cm.BuGn,'YlGn': plt.cm.YlGn,'binary': plt.cm.binary,
		'gist_yarg': plt.cm.gist_yarg,'gist_gray': plt.cm.gist_gray,
		'gray': plt.cm.gray,'bone': plt.cm.bone,
		'pink': plt.cm.pink,'spring': plt.cm.spring,'summer': plt.cm.summer,
		'autumn': plt.cm.autumn,'winter': plt.cm.winter,'cool': plt.cm.cool,
		'Wistia': plt.cm.Wistia,'hot': plt.cm.hot,'afmhot': plt.cm.afmhot,
		'gist_heat': plt.cm.gist_heat,'copper': plt.cm.copper,
		'PiYG': plt.cm.PiYG,'PRGn': plt.cm.PRGn,'BrBG': plt.cm.BrBG,
		'PuOr': plt.cm.PuOr,'RdGy': plt.cm.RdGy,'RdBu': plt.cm.RdBu,
		'RdYlBu': plt.cm.RdYlBu,'RdYlGn': plt.cm.RdYlGn,
		'Spectral': plt.cm.Spectral,'coolwarm': plt.cm.coolwarm,
		'bwr': plt.cm.bwr,'seismic': plt.cm.seismic,
		'twilight': plt.cm.twilight,'twilight_shifted': plt.cm.twilight_shifted,
		'hsv': plt.cm.hsv,'Pastel1': plt.cm.Pastel1,'Pastel2': plt.cm.Pastel2,
		'Paired': plt.cm.Paired,'Accent': plt.cm.Accent,'Dark2': plt.cm.Dark2,
		'Set1': plt.cm.Set1,'Set2': plt.cm.Set2,'Set3': plt.cm.Set3,
		'tab10': plt.cm.tab10,'tab20': plt.cm.tab20,'tab20b': plt.cm.tab20b,
		'tab20c': plt.cm.tab20c,'flag': plt.cm.flag,'prism': plt.cm.prism,
		'ocean': plt.cm.ocean,'gist_earth': plt.cm.gist_earth,
		'terrain': plt.cm.terrain,'gist_stern': plt.cm.gist_stern,
		'gnuplot': plt.cm.gnuplot,'gnuplot2': plt.cm.gnuplot2,
		'CMRmap': plt.cm.CMRmap,'cubehelix': plt.cm.cubehelix,'brg': plt.cm.brg,
		'gist_rainbow': plt.cm.gist_rainbow,'rainbow': plt.cm.rainbow,
		'jet': plt.cm.jet,'turbo': plt.cm.turbo,
		'nipy_spectral': plt.cm.nipy_spectral,'gist_ncar': plt.cm.gist_ncar
	}
	return cmaps


def print_colormaps():
	colormaps = return_cmaps()
	print("Available colormaps are:")
	print(tuple(colormaps.keys()))


def set_colormap(argcolormap):
	"""Used in plot_scatter(). Sets values like colormap, fontsize etc."""
	colormaps = return_cmaps()

	try:
		colormap = colormaps[argcolormap]
	except KeyError:
		raise ColormapError(argcolormap)
	else:
		return colormap


def save_graph(path, bbox_inches):
	"""Called in graph functions."""
	# If a path for the save was not provided, save the current
	# dataset with the suffix in json_files/file_count.json.
	if not path:
		# Read the count in file_count.json
		with open('json_files/file_count.json', 'r') as f_obj:
			current_count = f_obj.read()
			save_file = 'saved_graphs/graph_' + current_count + '.png'

		# Increment the file_count by 1.
		with open('json_files/file_count.json', 'w') as f_obj:
			f_obj.write(str(int(current_count) + 1))

		# Save the graph.
		plt.savefig(save_file, bbox_inches=bbox_inches)
		print("Saved the graph in {}".format(save_file) + ".")

	# Else, save the file in the provided directory.
	else:
		# Save the dataset in the provided path.
		plt.savefig(path, bbox_inches)
		print("Saved the graph in {}".format(path) + ".")


def plot_scatter(dataset, dataset2, colormap, title, save, path, bbox_inches):
	"""Draws a scatter plot graph using matplotlib. Used in scatter_dataset()"""
	if not dataset2:
		indices = list(range(1, len(dataset) + 1))
	else:
		indices = dataset2

	cmap = set_colormap(colormap)
	plt.scatter(indices, dataset, c=indices, 
		cmap=cmap, edgecolor='none', s=10)

	plt.title(title, fontsize=24)
	plt.xlabel("Element Index", fontsize=14)
	plt.ylabel("Dataset Value", fontsize=14)

	# Set size of tick labels.
	plt.tick_params(axis='both', which='major', labelsize=14)

	# Set the range for each axis.
	plt.axis([1, len(indices), 0, max(dataset)])

	# Save the graph or not.
	if save:
		save_graph(path, bbox_inches)
	elif not save:
		pass
	else:
		raise SaveError

	# Draw the graph.
	plt.show()
	


def draw_line_graph(dataset, dataset2, title, save, path, bbox_inches):
	"""Draws a line graph, called in line_graph()."""
	if not dataset2:
		x_values = list(range(1, len(dataset) + 1))
	else:
		x_values = dataset2

	plt.plot(x_values, dataset)

	# Set chart title and label axes.
	plt.title(title, fontsize=24)
	plt.xlabel("Element Index", fontsize=14)
	plt.ylabel("Dataset Value", fontsize=14)

	# Set size of tick labels.
	plt.tick_params(axis='both', labelsize=14)

	# Save the graph or not.
	if save:
		save_graph(path, bbox_inches)
	elif not save:
		pass
	else:
		raise SaveError

	# Draw the graph.
	plt.show()


def reprstr_method(dataset, path):
	args = namedtuple('DataVisualysis', 'dataset, path')
	representation = str(args(dataset, path))
	return representation


def raise_method_error(method):
	"""Raises a MethodError exception when called."""
	raise MethodError(method)


def raise_mode_include_error(mode_include):
	"""Raises a ModeIncludeError exception when called."""
	raise ModeIncludeError(mode_include)