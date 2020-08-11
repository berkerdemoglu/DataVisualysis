import requests
import json

def get_random_numbers(numbers, mini, maxi, replacement, method):
		# Get a new random number list using random.org
		filename = 'json_files/numbers_data.json'
		url = 'https://api.random.org/json-rpc/1/invoke'
		data = {
		    "jsonrpc": "2.0",
		    "method": method,
		    "params": {
		        "apiKey": "redacted", # redacted, enter your own API Key.
		        "n": numbers,
		        "min": mini,
		        "max": maxi,
		        "replacement": replacement
		    },
		    "id": 42
		}
		params = json.dumps(data)
		response = requests.post(url, params)

		# Store the generated numbers in a .json file in string format.
		data_index = response.text.index("data")
		completion_index = response.text.index("completion")
		stored_data = response.text[data_index + 6:completion_index - 2]
		with open(filename, 'w') as file:
			json.dump(stored_data, file)