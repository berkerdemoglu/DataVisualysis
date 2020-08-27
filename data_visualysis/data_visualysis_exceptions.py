# The exceptions used in data_visualysis_functions.py.

class NTypeError(Exception):
	"""Exception raised when ntype for (create_dataset_random_module()) is invalid."""

	def __init__(self, message="Invalid input for ntype"):
		super().__init__(message)

class CountNotIntegerError(Exception):
	"""Exception raised when count (reset_count()) is not an integer."""

	def __init__(self, message="count must be an integer"):
		super().__init__(message)

class RandomOrgError(Exception):
	"""Exception raised when random.org generates an error."""

	def __init__(self, message="random.org generated an error"):
		super().__init__(message)

class InvalidAPIKeyError(Exception):
	"""Exception raised when an invalid random.org API key is provided."""

	def __init__(self, message="Invalid API key"):
		super().__init__(message)

class NotEnoughBitsError(Exception):
	"""Exception raised when there aren't enough bits 
	available in the provided random.org API key."""

	def __init__(self, message="Not enough bits available"):
		super().__init__(message)

class InvalidStoredPathError(Exception):
	"""Exception raised when the stored path is not a string."""

	def __init__(self, message="The path provided is invalid"):
		super().__init__(message)

class MethodError(Exception):
	"""Exception raised when method is not 'store' or 'return'."""

	def __init__(self, method, message="method must be 'store' or 'return': "):
		super().__init__(message + "method cannot be '{}'".format(method))

class ModeIncludeError(Exception):
	"""Exception raised when mode_include is not 'include' or 'exclude'."""

	def __init__(self, mode_include, message="mode_include must be 'true' or 'false': "):
		super().__init__(message + "mode_include cannot be '{}'".format(mode_include))

class ColormapError(Exception):
	"""Exception raised when mode_include is not 'include' or 'exclude'."""

	def __init__(self, colormap, message="No such color map"):
		super().__init__(message + " as '{}'".format(colormap))