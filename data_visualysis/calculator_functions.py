def sqrt(n):
    """Returns the square root value of a number."""
    n = float(n)
    n = n ** (1/2)
    return n


def sq(n):
	"""Returns the squared value of a number."""
	n = float(n)
	n = n ** 2
	return n


def find_mean(number_list):
	"""Finds the mean of a list of numbers. 
	Rounds up two decimal places."""
	return float(format(sum(number_list) / len(number_list), '.2f'))


def find_median(number_list):
	"""Finds the median of a list of numbers."""
	sorted_number_list = sorted(number_list)
	list_length = len(sorted_number_list)

	# Check if list_length is even or odd.
	if list_length % 2 != 0:
		# if odd:
		median_position = int(list_length / 2)
		median = sorted_number_list[median_position]
	else:
		# if even:
		middle_score_1_index = int(list_length / 2) - 1
		middle_score_2_index = int((list_length / 2)) 
		median = (number_list[middle_score_1_index] + number_list[middle_score_2_index]) / 2

	return median


def find_mode(number_list, occurrence="no"):
	"""Finds the mode of a list of numbers."""
	# Sort the list, store the length of the list in a variable, 
	# create a dictionary named counts and create a copy of number_list.
	original_list = number_list[:]
	sorted_number_list = sorted(number_list)
	list_length = len(sorted_number_list)
	counts = {}
	# Find how many times a number occurs in the list.
	for i in range(0, list_length):
		count = 0 # Reset the counter in every loop.
		while sorted_number_list[i] in original_list:
			# Keep track of the occurences of each unique number.
			original_list.remove(sorted_number_list[i])
			count += 1
			counts[sorted_number_list[i]] = count

	# Create a list containing the occurrences of each number.
	occurrences = [n for n in counts.values()]
	# Create a list containing each unique number.
	occuring_numbers = [n for n in counts.keys()]
	# Check if there is a number that occurs more than once.
	if max(occurrences) != 1:
		# Find the index of the mode and the mode.
		mode_index = occurrences.index(max(occurrences))
		mode = occuring_numbers[mode_index]

		# Return only the mode or return a list containing the mode
		# and how many times it occurs.
		if occurrence == 'yes': # If user has specified a value for count.
			return [mode, max(occurrences)]
		else: # Default option.
			return mode # Integer value.
	else:
		return "The list has no mode."


def find_standard_deviation(number_list):
	"""Finds the standard deviation of a list of numbers."""
	mean = find_mean(number_list)
	distances = []
	for num in number_list:
		distance = num - mean
		if distance < 0: # if negative, make it positive.
			distance = -distance

		distances.append(sq(distance))

	return float(format(sqrt(sum(distances) / len(number_list)), '.4f'))


def find_variance(number_list):
	"""Finds the variance of a list of numbers."""
	return float(format(find_standard_deviation(number_list) ** 2, '.4f'))


def find_percentile(number_list, percentile):
	sorted_number_list = sorted(number_list)
	list_length = len(number_list)
	index = int(round((percentile * list_length/100) + 0.5))
	return number_list[index - 1]