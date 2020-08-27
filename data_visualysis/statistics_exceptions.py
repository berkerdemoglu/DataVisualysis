# The exceptions used in statistics_functions.py.

class OccurrenceError(Exception):
	"""Exception raised when occurrence (find_mode()) is not 'yes' or 'no'."""

	def __init__(self, occurrence, 
		message="occurrence must be 'yes' or 'no': "):
		super().__init__(message + "occurrence cannot be {}".format(occurrence))