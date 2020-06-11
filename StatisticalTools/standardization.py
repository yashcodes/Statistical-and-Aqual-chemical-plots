"""
Generate a csv file 'standardization.csv' containing standardized data
"""
import os
import pandas as pd 
import statistics as stat

def standardization(data_fn, decimal = 2):

	reader = pd.read_csv(data_fn)
	var_name = reader.iloc[:, 0].name 
	data = reader.iloc[:, 0].values

	mean = stat.mean(data)
	stand_data = [round(value - mean, decimal) for value in data]

	df = pd.DataFrame(stand_data, index = range(0, len(stand_data)), columns = ['Standardized_' + var_name])

	df = pd.concat([reader, df], axis = 1)

	cwd = os.getcwd()
	fn = cwd + '/' + 'standrdized_data.csv'
	df.to_csv(fn, index=False)
	print(stand_data)
	
	return 0