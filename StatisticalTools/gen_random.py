"""
Generate a csv file 'random_nums.csv' containing 'nums' random numbers in between 'new_min' and 'new_max'  
"""

import os
import random
import pandas as pd

def rand(nums, new_min, new_max, decimal = 2):

	data = [round(random.uniform(new_min, new_max), decimal) for i in range(nums)]
	df = pd.DataFrame(data, columns = ['Random Nums'])

	cwd = os.getcwd()
	fn = cwd + '/' + 'random_nums.csv'
	df.to_csv(fn, index=False)
	print(data)

	return 