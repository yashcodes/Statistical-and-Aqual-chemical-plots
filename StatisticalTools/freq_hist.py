
import pandas as pd
import statistics as stat
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def histogram_for_single_varibale(column, bins_list = None, log_scale = False):

	plt.title('Frequency histogram for variable ' + column.name)

	# Plotting Histogram

	a = column.values
	
	if bins_list != None:
		N, bins, patches = plt.hist(a, bins = bins_list, edgecolor='k', color = 'w')
	else:
		N, bins, patches = plt.hist(a, edgecolor='k', color = 'w')

	N_max = N.max()

	if log_scale == True:
		plt.xscale('log')
		plt.text(min(a), N_max, 'Logarithmic Scale', color = "r")

	plt.text(min(a), N_max, 'Linear Scale')

	plt.xlabel(column.name)
	plt.ylabel('Frequency')

	# Coloring histogram 

	fracs = N / N.max()

	norm = colors.Normalize(fracs.min(), fracs.max())

	for thisfrac, thispatch in zip(fracs, patches):
		color = plt.cm.viridis(norm(thisfrac))
		#thispatch.set_facecolor(color)
		thispatch.set_hatch('/////')
		thispatch.set_edgecolor(color)

	# Plotting statistics of data

	mean = round(stat.mean(a), 2)
	stdev = round(stat.stdev(a), 2)
	a_max = max(a)

	plt.axvline(mean, 0, N_max, color = "r")
	plt.text(mean, N_max, 'Mean\n(' + str(mean) +')', color = "b")
	m_std = mean + stdev
	i = 1    
	while (m_std <= a_max):
		plt.axvline(m_std, 0, N_max, color = "r")
		plt.text(m_std, N_max, 'Mean + ' + str(i) + 'Std\n(' + str(m_std) + ')', color = "b")
		m_std = m_std + stdev
		i = i + 1

	a_min = min(a)
	m_std = mean - stdev
	i = 1  
	while (a_min <= m_std):
		plt.axvline(m_std, 0, N_max, color = "r")
		plt.text(m_std, N_max, 'Mean - ' + str(i) + 'Std\n(' + str(m_std) + ')', color = "b")
		m_std = m_std - stdev
		i = i + 1

	return

def plot_histograms_multi_fig(data_fn, bins_list = None, log_scale = False):

	df = pd.read_csv(data_fn)

	i = 1
	for column in df:
		plt.figure(i)
		histogram_for_single_varibale(df[column], bins_list = bins_list, log_scale = log_scale)
		i = i + 1
	plt.show()
	
	return 0

def plot_histograms_sing_fig(data_fn, bins_list = None, log_scale = False):

	df = pd.read_csv(data_fn)

	i = 211
	for column in df:
		plt.subplot(i)
		histogram_for_single_varibale(df[column], bins_list = bins_list, log_scale = log_scale)
		i = i + 1
	plt.show()

	return 0