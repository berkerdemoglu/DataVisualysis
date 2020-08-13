# The exceptions used in data_modeler_functions.py.

class NTypeError(Exception):
	"""Exception raised when ntype for (create_dataset_random_module()) is invalid."""

	def __init__(self, method, message="Invalid input for ntype"):
		self.method = method
		self.message = message
		super().__init__(self.message)

class CountNotIntegerError(Exception):
	"""Exception raised when count (reset_count()) is not an integer."""

	def __init__(self, count, message="count must be an integer"):
		self.count = count
		self.message = message
		super().__init__(self.message)

class RandomOrgError(Exception):
	"""Exception raised when invalid inputs are provided in grn()."""

	def __init__(self, message="Invalid input for generate_random_dataset()"):
		self.message = message
		super().__init__(self.message)

class InvalidPathError(Exception):
	"""Exception raised when count (reset_count()) is not an integer."""

	def __init__(self, message="The path stored in json_files/default_directory.json is not a string."):
		self.message = message
		super().__init__(self.message)