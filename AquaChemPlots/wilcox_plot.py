import matplotlib.pyplot as plot
import matplotlib.text as txt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
from matplotlib.offsetbox import AnchoredText
import numpy as np
import pandas as pd
import random
import math

def wilcox_plot(data_fn):

	reader = pd.read_csv(data_fn)
	SAR = reader.iloc[:, 1].values
	cond = reader.iloc[:, 2].values
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

	fig, plt = plot.subplots()
	x = np.linspace(100 , 5000 , 100)

	y1 = -0.0015816 * x + 10.15816
	y2 = -0.0022959 * x + 18.22959
	y3 = -0.0030102 * x + 26.30102
	plt.plot(x, y1, '#dae1e7' )
	plt.plot(x, y2, '#00909e' )
	plt.plot(x, y3, '#27496d' )
	plt.fill_between(x, 0 , y1, facecolor= '#dae1e7' )
	plt.fill_between(x, y1, y2, facecolor= '#00909e' )
	plt.fill_between(x, y2, y3, facecolor= '#27496d' )
	plt.fill_between(x, y3, 27 , facecolor= '#142850' )
	plt.axvline(x= 250 , color= 'black' )
	plt.axvline(x= 750 , color= 'black' )
	plt.axvline(x= 2250 ,color= 'black' )

	scatter = []
	keys = []
	for key in this_dict:
		i = this_dict[key][0]
		j = this_dict[key][1] 
		scatter.append(plot.scatter(cond[i:j+1], SAR[i:j+1]))
		keys.append(key + " sample")
	
	colors = [scatter[i].get_facecolors()[0].tolist() for i in range(len(scatter))]
	
	plot.xlabel( "Electric Conductivity (10^-6 S/cm)")
	plot.ylabel( "Sodium Absorbtion Ratio (SAR)" )
	plt.legend(loc= 'upper left' )
	legends = [Rectangle(( 0 , 0 ), 1 , 1 , fc= '#dae1e7' , alpha= 0.5 ), Rectangle(( 0 , 0 ), 1 , 1 , fc= '#00909e' , alpha= 0.5 ), Rectangle(( 0 , 0 ), 1 , 1 , fc= '#27496d' , alpha= 0.5 ), Rectangle(( 0 , 0 ), 1 , 1 , fc= '#142850' , alpha= 0.5 )]
	marker = [Line2D(range(0), range(0), color="white", marker='o', markerfacecolor=color) for color in colors]
	legends.extend(marker)

	text_list = ["Low Sodium Hazard" , "Medium Sodium Hazard" ,
	"High Sodium Hazard" , "Very High Sodium Hazard"]

	text_list.extend(keys)
	plt.legend(legends, text_list)
	plot.xticks([250, 750, 2250], ['250', '750', '2250'])
	
	anchored_text = AnchoredText("STABILITY HAZARD\n(all values in 10^-6 S/cm)\nLow: 0 < x <250\nMedium: 250 < x < 750\nHigh: 750 < x < 2250\nVery High: 2250 < x", loc=4)
	plt.add_artist(anchored_text)

	plot.show()

	return