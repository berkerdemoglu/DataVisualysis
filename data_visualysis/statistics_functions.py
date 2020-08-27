from statistics_exceptions import *
from collections import Counter

def find_occurrences(number_list):
	"""Finds how many times every number in a list occurs."""
	counter = Counter(number_list)
	occurrences = counter.most_common()
	return occurrences

def find_mode(number_list, occurrence="no"):
	"""Finds the mode of a list of numbers."""
	# Return counts by calling the find_occurrences function.
	counts = find_occurrences(number_list)

	# Create a list containing the occurrences of each number and
	# Create a list containing each unique number.
	occurrences = []; occuring_numbers = []
	for number, n_occurrence in counts:
		occurrences.append(n_occurrence)
		occuring_numbers.append(number)

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


#########################################
################ TESTING ################
#########################################

if __name__ == "__main__":
	dataset = [1, 2, 5, 1, 3, 2, 4, 1]
	o = find_occurrences(dataset)
	m = find_mode(dataset)
	print(m)