import os
import pandas as pd

def normalize(data_fn, new_min, new_max, decimal = None):

	reader = pd.read_csv(data_fn)

	new_diff = new_max - new_min

	normalized_data = []
	name = []
	for column in reader:

		name.append('Normalized_' + reader[column].name)
		min_d = min(reader[column].values)
		max_d = max(reader[column].values)
		diff_d = max_d - min_d

		temp = []
		for value in reader[column].values:
			normalized_value = ((value - min_d) * (new_diff) / (diff_d)) + new_min
			temp.append(round(normalized_value, decimal) if decimal else normalized_value)

		normalized_data.append(temp)

	dfs = []
	for i in range(0, len(normalized_data)):
		dfs.append(pd.DataFrame(normalized_data[i] , index = range(0, len(normalized_data[i])), columns =  name))

	df = pd.concat(dfs, axis = 1)
	df = pd.concat([reader, df], axis = 1)
	cwd = os.getcwd()
	fn = cwd + '/' + 'norm_data.csv'

	df.to_csv(fn, index=False)
	print(normalized_data)
	return 0