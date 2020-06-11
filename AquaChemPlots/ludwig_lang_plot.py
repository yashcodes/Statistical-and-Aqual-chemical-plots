import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def ludwig_lang_plot(cation_data_fn, anion_data_fn, cations, anions):

	cat_reader = pd.read_csv(cation_data_fn)
	an_reader = pd.read_csv(anion_data_fn)

	cat_data = []
	for column in cat_reader:
		cat_data.append(cat_reader[column].values)
	samp_names = cat_data[0]

	cat_names = []
	for i in cations:
		cat_names.append(cat_reader.iloc[:,i].name)
	xlabel = cat_names[0]
	for i in range(1, len(cat_names)):
		xlabel = xlabel + '+' + cat_names[i]
	
	an_names = []
	for i in anions:
		an_names.append(an_reader.iloc[:,i].name)
	ylabel = an_names[0]
	for i in range(1, len(an_names)):
		ylabel = ylabel + '+' + an_names[i]
	
	an_data = []
	for column in an_reader:
		an_data.append(an_reader[column].values)

	x = 50 * sum(cat_data[i] for i in cations)/sum(cat_data[1:])
	y = 50 * sum(an_data[i] for i in anions)/sum(an_data[1:])

	this_dict = {}

	k = 0
	temp_name = samp_names[0]	
	for i in range(len(samp_names)):
		if type(samp_names[i]) == str:
			this_dict[temp_name] = [k, i-1]
			temp_name = samp_names[i]
			k = i
	this_dict[temp_name] = [k, len(samp_names)-1]

	for key in this_dict:
		i = this_dict[key][0]
		j = this_dict[key][1] 
		plt.scatter(x[i:j+1], y[i:j+1], label = key)

	plt.grid(True, which = "both")
	plt.title("Ludwig-Langelier Plot")
	plt.xlabel(xlabel + " (% of 50 millieq)" )	
	plt.ylabel(ylabel + " (% of 50 millieq)")
	plt.legend()
	plt.show()

	return