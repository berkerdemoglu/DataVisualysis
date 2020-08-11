from data_modeler import DataModeler
import json

# filename = 'json_files/numbers_data.json'
# with open(filename, 'r') as file:
# 	loaded_file = (json.load(file)).strip('[]').replace('"', '').replace(' ', '').split(',')
# 	dataset = [int(n) for n in loaded_file]

data_modeler = DataModeler()

# data_modeler.create_random_number_dataset(10000, 100, 280)
data_modeler.print_results()
