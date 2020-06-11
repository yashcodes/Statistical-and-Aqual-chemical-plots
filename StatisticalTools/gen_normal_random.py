"""
Generate 'nums' noramlly distributed random numbers having given 'mean' and standard deviation 'std_dev'
"""
import os
import pandas as pd
import numpy as np

def normal_rand(nums, mean, std_dev, decimal = 2):

	data = np.random.normal(mean, std_dev, nums)
	round_data = [round(value, decimal) for value in data]

	df = pd.DataFrame(round_data, columns = ['Normal Random Nums'])

	cwd = os.getcwd()
	fn = cwd + '/' + 'norm_random_nums.csv'
	df.to_csv(fn, index=False)
	print(round_data)

	return 