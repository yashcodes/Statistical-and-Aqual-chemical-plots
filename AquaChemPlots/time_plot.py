import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import pandas as pd
import random

def time_plot(cation_data_fn, anion_data_fn):

	cat_data = pd.read_csv(cation_data_fn)
	an_data = pd.read_csv(anion_data_fn)

	if cat_data.shape != an_data.shape:
		raise Exception("Data is not in correct format")

	cat_names = cat_data.iloc[:, 0].values
	an_names =  an_data.iloc[:, 0].values
	ion_names = np.concatenate((cat_names, an_names))

	days = cat_data.shape[1] - 1

	plt.axvline(x= 0 , color= 'black' )

	colours_used = []
	for day in range(1 , days+1):
		col = "#" + '' .join([random.choice( '0123456789ABCDEF' ) for j in range( 6 )])
		colours_used.append(col)

		cat_concs = cat_data.iloc[:, day].values
		an_concs =  an_data.iloc[:, day].values

		coord = []
		k = 5

		for conc in cat_concs:
			coord.append([conc, k])
			plt.axhline(y=k, color = 'black' , linestyle= 'dashed')
			plt.scatter(conc, k, s= 20 , color = col)
			k = k + 5

		k = k -5

		for i in range(len(an_concs) -1 , -1 , -1 ):
			coord.append([ -1 *(an_concs[i]), k])
			plt.scatter( -1 *(an_concs[i]), k, s= 20 , color = col)
			k = k - 5

		coord.append(coord[0])

		xs, ys = zip(*coord)

		plt.plot(xs, ys, color = col)
		
		plt.plot([coord[0][0], coord[1][0]], [coord[0][1], coord[1][1]], color = col, label = 'day' + ' ' +str(day))
		for i in range( 1 , len(coord) -1 ):
			plt.plot([coord[i][0], coord[i+ 1 ][0]], [coord[i][1],coord[i+ 1][1]], color = col)

	plt.xlabel( "Concentration in milli-eqivalents" , fontsize = 'large')
	plt.title('Time Plot', fontsize = 'x-large')
	plt.legend(loc = 'upper right' )
	for i in range(len(coord) -1 ):
		plt.text(coord[i][ 0 ], coord[i][ 1 ], ion_names[i], color = '#30475e', fontsize = 'large')

	plt.show()
	return 
