import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

def mwl_plot(data_fn):

	reader = pd.read_csv(data_fn)
	O18 = reader.iloc[:, 1].values
	H2 = reader.iloc[:, 2].values
	samp_names = reader.iloc[:, 0].values
	this_dict = {}

	k = 0
	temp_name = samp_names[0]	
	for i in range(len(samp_names)):
		if type(samp_names[i]) == str:
			this_dict[temp_name] = [k, i-1]
			temp_name = samp_names[i]
			k = i
	this_dict[temp_name] = [k, len(samp_names)-1]

	y = 8.2 * O18 + 10.8
	plt.plot(O18, y, 'black', label = "Eq : y = 8.2 * x + 10.8")
	plt.grid(True, which = "both")
	plt.title("Metoric Water Line")
	SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
	SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
	xlabel = "δ18O".translate(SUP)
	plt.xlabel(xlabel + "(0".translate(SUP)+ "/00)".translate(SUB))
	ylabel = "δ2H".translate(SUP)
	plt.ylabel(ylabel + "(0".translate(SUP)+ "/00)".translate(SUB))
	for key in this_dict:
		i = this_dict[key][0]
		j = this_dict[key][1] 
		plt.scatter(O18[i:j+1], H2[i:j+1], label = key)
	plt.legend()
	plt.show()
	
	return
