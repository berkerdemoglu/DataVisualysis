from math import sqrt
from statistics_exceptions import *


def find_mean(number_list):
	"""Finds the mean of a list of numbers. 
	Rounds up two decimal places."""
	# Sum up all the numbers in the list and divide it by the length of the list.
	return float(format(sum(number_list) / len(number_list), '.2f')) # Return the mean.


def find_median(number_list):
	"""Finds the median of a list of numbers."""
	# Create a sorted copy of the list of numbers
	# and store the length of the list in a variable.
	sorted_number_list = sorted(number_list)
	list_length = len(sorted_number_list)

	# If list_length is odd:
	if list_length % 2 != 0:
		median_position = int(list_length / 2)
		median = sorted_number_list[median_position]

	# If list_length is even:
	else:
		middle_score_1_index = int(list_length / 2) - 1
		middle_score_2_index = int((list_length / 2)) 
		median = (number_list[middle_score_1_index] + number_list[middle_score_2_index]) / 2

	return median # Return the median.


def find_occurrences(number_list):
	"""Finds how many times every number in a list occurs."""
	# Sort the list, store the length of the list in a variable, 
	# create a dictionary to store the occurrences of each number 
	# and create a copy of number_list.
	original_list = number_list[:]
	sorted_number_list = sorted(number_list)
	list_length = len(sorted_number_list)
	counts = {}

	# Find how many times a number occurs in the list.
	for i in range(0, list_length):
		count = 0 # Reset the count in every loop.
		while sorted_number_list[i] in original_list:
			# Record how many times each number occurs in the list.
			original_list.remove(sorted_number_list[i])
			count += 1
			counts[sorted_number_list[i]] = count
			
	return counts # Return the dictionary that stores occurrences of each number.

def find_mode(number_list, occurrence="no"):
	"""Finds the mode of a list of numbers."""
	# Return counts by calling the find_occurrences function.
	counts = find_occurrences(number_list)

	# Create a list containing the occurrences of each number and
	# Create a list containing each unique number.
	occurrences = [n for n in counts.values()]
	occuring_numbers = [n for n in counts.keys()]

	# If the most common number occurs more than once, execute the code below.
	if max(occurrences) != 1:
		# Find the index of the mode and the mode itself.
		mode_index = occurrences.index(max(occurrences))
		mode = occuring_numbers[mode_index]

		# Return only the mode or return a list containing the mode
		# and how many times it occurs or raise an error.

		# If user has entered 'yes' for occurrence:
		if occurrence == 'yes':
			return [mode, max(occurrences)]
		# If user has entered 'no' for occurrence:
		elif occurrence == 'no': # 
			return mode
		# If user has entered an invalid value for occurrence:
		else:
			raise OccurrenceError(occurrence)

	# If not, raise an error.
	else:
		return "The list has no mode."


def find_standard_deviation(number_list):
	"""Finds the standard deviation of a list of numbers."""
	# Calculate the mean of the list.
	mean = find_mean(number_list)
	# Create a list to store the squared distance of each number to the mean.
	sq_distances = []
	for num in number_list:
		# Calculate the distance of the number to the mean.
		distance = num - mean
		# Take absolute value of the distance.
		if distance < 0:
			distance = -distance

		# Add the squared value of the distance to sq_distances.
		sq_distances.append(distance ** 2)

	# Return the standard deviation of the list.
	return float(format(sqrt(sum(sq_distances) / len(number_list)), '.4f'))


def find_variance(number_list):
	"""Finds the variance of a list of numbers."""
	# Variance = Standard deviation squared
	# Return squared value of the standard deviation of the list.
	return float(format(find_standard_deviation(number_list) ** 2, '.4f'))


def find_percentile(number_list, percentile):
	# Create a sorted copy of the list.
	sorted_number_list = sorted(number_list)
	# Store the length of the list in a variable.
	list_length = len(sorted_number_list)
	# The formula for finding the percentile and returning the value.
	index = (percentile / 100) * (list_length + 1)
	return sorted_number_list[int(index - 1)]