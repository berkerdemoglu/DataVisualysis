# import <module_name>
"""Test the speed of a code snippet. Import a file and run a function.
The results will be stored in a directory you specify."""

filename = 'json_files/' # Enter save directory
with open(filename, 'w') as f:
	exec_times = []
	for i in range(1, 31):
		start_time = time.time()
		# YOUR CODE(function) HERE
		exec_times.append(float("{}".format((time.time() - start_time))))
	json.dump(exec_times, f)