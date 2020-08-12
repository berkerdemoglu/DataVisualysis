import json
import requests

def grn(numbers=100):
	"""Get a new random number list using random.org and save it in 
	json_files/numbers_data.json. 'grn' is short for generate random numbers."""
	# Get numbers from random.org.
	url = 'https://api.random.org/json-rpc/1/invoke'
	data = {
	    "jsonrpc": "2.0",
	    "method": "generateIntegers",
	    "params": {
        "apiKey": "c05fccde-4fb0-48de-8b50-65a0840604fd",
	    "n": numbers,
		"min": 0,
		"max": 100,
		"replacement": "true"
		},
		"id": 42
		}
	params = json.dumps(data)
	response = requests.post(url, params)
	# Store the generated numbers in a .json file list format with integer elements.
	with open('../json_files/request_random.json', 'w') as f:
		json.dump(response.text, f)

grn()

with open('../json_files/request_random.json', 'r') as f:
	content = json.load(f)

if 'error' in content:
	print("Yes")
else:
	print("No")