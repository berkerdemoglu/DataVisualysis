import sys
sys.path.append('../')

import json

from data_visualysis import DataModeler

def main():
	filename = 'covid_turkey.json'
	with open(filename, 'r') as f_obj:
		contents = json.load(f_obj)

	result_lists = [list() for i in range(4)]

	for daily_result in contents.values():
		result_lists[0].append(daily_result['Tests'])
		result_lists[1].append(daily_result['Cases'])
		result_lists[2].append(daily_result['Deaths'])
		result_lists[3].append(daily_result['Healed'])

	data_modeler = DataModeler(dataset=[1])
	title_num = 0
	for result_list in result_lists:
		title_num += 1
		if title_num == 1:
			title = "Tests"
		elif title_num == 2:
			title = "Cases"
		elif title_num == 3:
			title = "Deaths"
		else:
			title = "Healed"

		data_modeler.dataset = result_list
		data_modeler.calculate.dataset = result_list
		print("\nNow analyzing", title, "results:\n")
		data_modeler.show_results(mode_occurrence=True)
		data_modeler.line_graph(title=title)


	new_dataset = []
	for test, case in zip(result_lists[0], result_lists[1]):
		new_dataset.append(test / case)

	data_modeler.dataset = new_dataset
	data_modeler.line_graph(title="Test/Case Per Day")


if __name__ == '__main__':
	main()