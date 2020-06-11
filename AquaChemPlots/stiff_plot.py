import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def stiff_plot(data_fn):
	reader = pd.read_csv(data_fn)
	
	cat_concs = reader.iloc[:, 2].values
	cat_names = reader.iloc[:, 1].values

	an_concs = reader.iloc[:, 4].values
	an_names = reader.iloc[:, 3].values

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

	spacing = 5

	plt.axvline(x= 0, c = 'black')

	for key in this_dict:

		ion_names = np.concatenate((cat_names[this_dict[key][0]: this_dict[key][1] + 1], an_names[this_dict[key][0]: this_dict[key][1] + 1]))
		coord = []
		k = spacing
		for cat_conc in cat_concs[this_dict[key][0]: this_dict[key][1] + 1]:
			coord.append([cat_conc, k])
			plt.axhline(y=k, color = 'black' , linestyle= 'dashed' )
			k = k + 5
		plt.text(0, (spacing + k - 5)/2, key , fontsize = 'x-large')
		spacing = k

		k = k - 5

		for an_conc in an_concs[this_dict[key][0]: this_dict[key][1] + 1]:
			coord.append([ -1 * an_conc, k])
			k = k - 5

		coord.append(coord[0])
		
		xs, ys = zip(*coord)
		plt.plot(xs, ys, 'ro')
		x = []
		y = []
		for i in range(len(coord) -1 ):
			plt.plot([coord[i][0], coord[i+ 1 ][0]], [coord[i][ 1 ], coord[i+ 1 ][ 1 ]], 'black')
			x.append(coord[i][0])
			y.append(coord[i][1])
			plt.text(coord[i][0], coord[i][1] ,ion_names[i], fontsize = 'large')

		plt.fill(x, y, label = key )

	plt.xlabel( "Concentration in milli-eqivalents" , fontsize = 'large')
	plt.title('Stiff Plot', fontsize = 'x-large')
	plt.legend()
	plt.show()

	return
