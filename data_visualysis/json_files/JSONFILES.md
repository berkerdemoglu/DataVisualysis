# What is the json_files folder?

- The json_files folder contains the files required for functionality.
- Please ***DO NOT*** change the folder or the files inside before you read the part below.

## api_key.json
api_key.json contains the API key required to generate a dataset containing random integers using random.org.
To use random data generation using random.org, you must get an API key from random.org. To do that, follow the instructions below:

1. Signup and login to random.org
2. Go to [random.org](https://api.random.org/dashboard)
3. Click on 'Create a New API Key'

Keep in mind that you can write the API key using a method from DataVisualysis or manually. If you are writing the new API key manually, be sure to use double quotes ("").

## default_directory.json
default_directory.json stores the default directory to store randomly generated datasets using either the random module or random.org. You can call a method from DataVisualysis to change the default directory or you can do it manually. Be sure to use double quotes ("") if writing manually.


## file_count.json
file_count.json stores the number of files created by DataVisualysis. When saving a dataset, DataVisualysis will save it automatically with the suffix stored in file_count.json.  You can call a method from DataVisualysis to change the file count or you can do it manually.


## numbers_data.json
When a dataset is being generated either by the random module or by random.org, the default directory for the save is numbers_data.json. If a path for most methods in DataVisualysis is not provided, numbers_data.json will be used. Please **do not delete** this file or tamper with it.


## request_random.json
When a dataset using random.org's API is being generated, the response from random.org will be stored in request_random.json to check if random.org generated an error or to extract data from the response. This is another crucial file. Please **do not delete** this file or tamper with it.
