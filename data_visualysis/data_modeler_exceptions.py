# The exceptions used in data_modeler_functions.py.

class NTypeError(Exception):
	"""Exception raised when ntype for (create_dataset_random_module()) is invalid."""

	def __init__(self, method, message="Invalid input for ntype"):
		super().__init__(message)

class CountNotIntegerError(Exception):
	"""Exception raised when count (reset_count()) is not an integer."""

	def __init__(self, count, message="count must be an integer"):
		super().__init__(message)

class RandomOrgError(Exception):
	"""Exception raised when invalid inputs are provided in grn()."""

	def __init__(self, message="random.org generated an error"):
		super().__init__(message)

class InvalidAPIKeyError(Exception):
	"""Exception raised when an invalid API key is provided in grn()."""

	def __init__(self, message="Invalid API key"):
		super().__init__(message)

class NotEnoughBitsError(Exception):
	"""Exception raised when there aren't enough bits available in the provided API key."""

	def __init__(self, message="Not enough bits available"):
		super().__init__(message)

class InvalidPathError(Exception):
	"""Exception raised when count (reset_count()) is not an integer."""

	def __init__(self, message="The path stored in json_files/default_directory.json is not a string."):
		super().__init__(message)

class MethodError(Exception):
	"""Exception raised when method is not store or return."""

	def __init__(self, message="'method' must be 'store' or 'return'"):
		super().__init__(message)

class ModeIncludeError(Exception):
	"""Exception raised when method is not store or return."""

	def __init__(self, message="'mode_include' must be 'include' or 'exclude'"):
		super().__init__(message)