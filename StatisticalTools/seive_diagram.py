"""
Plot the seicve diagram and write summary about the grain sizes of each sample in 'seive_diag_summary.txt'
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def seive_diagram(data_fn):

	reader = pd.read_csv(data_fn)
	seive_symbols = reader.iloc[:, 0].values

	ns = len(reader.columns) - 1
	data = []
	sample_names = []
	remainders = []
	total_weights = []
	for i in range(1, ns + 1):
		data.append(list(reader.iloc[0:9, i].values))
		sample_names.append(reader.iloc[:, i].name)
		remainders.append(list(reader.iloc[9:10, i].values)[0])
		total_weights.append(list(reader.iloc[10:11, i].values)[0])
	
	# finding percentage retained of each sample
	per_ret = [[100 * (data[i][j]) / total_weights[i] for j in range(len(data[i]))] for i in range(len(data))]

	# finding cumulative percentage retained of each sample
	cum_per_ret = []
	for i in range(len(per_ret)):
		temp = []
		temp.append(per_ret[i][0])
		for j in range(1, len(per_ret[i])):
			temp.append(temp[-1] + per_ret[i][j])
		cum_per_ret.append(temp)
	
	# finding percentage finer of each sample 
	per_finer = [[100 - cum_per_ret[i][j] for j in range(len(cum_per_ret[i]))] for i in range(len(cum_per_ret))]
	
	x = [4.75, 2.36, 1.18, 0.6, 0.425, 0.30, 0.15, 0.045, 0.038]
	for i in range(len(x)):
		plt.axvline(x[i], 0, 100, color = "r",  linestyle='dashed') 
	
	for i in range(len(per_finer)):
		plt.semilogx(x, per_finer[i], label=sample_names[i])
		plt.scatter(x, per_finer[i])

	plt.grid(True, which = "both")	
	plt.xticks(x, ['4.75 (' + seive_symbols[0] + ')','2.36 (' + seive_symbols[1] + ')','1.18 (' + seive_symbols[2] + ')','0.6 (' + seive_symbols[3] + ')', '0.425 (' + seive_symbols[4] + ')', '0.30 (' + seive_symbols[5] + ')', '0.15 (' + seive_symbols[6] + ')', '0.045 (' + seive_symbols[7] + ')', '0.038 (' + seive_symbols[8] + ')'], rotation = 45)
	plt.ylabel('Percentage Finer (by weight)')
	plt.xlabel('Particle Size D, mm')
	plt.legend()
	plt.title('PARTICLE SIZE DISTRIBUTION CURVE (Particle Size D(mm) Vs Percentage finer)')

	#writing a summary .txt file 
	f = open("seive_diag_summary.txt", "w+")
	for i in range(len(sample_names)):
		f.write(sample_names[i] + '\n' + '\n')
		f.write('   Initial Dry Mass....' + str(total_weights[i]) + '\n')
		final_mass = sum(data[i]) + remainders[i]
		f.write('   Total Final Mass....' + str(final_mass) + '\n')
		mass_lost = total_weights[i] - final_mass
		per_mass_lost = (mass_lost / total_weights[i]) * 100
		f.write('   Mass Lost...........' + str(round(mass_lost, 2)) + ' (' + str(round(per_mass_lost, 2)) + '%)\n\n')
		f.write('      Screen     Screen      Mass                         Cumulative\n')
		f.write('       Name     Size (mm)   Retained     Retained(%)  Retained(%)  Finer(%)\n'  )
		f.write('   ----------- ----------- ----------   ------------ ------------ ----------\n')
		for j in range(len(x)):
			f.write('          %s      %s        %s          %s        %s        %s\n' %(seive_symbols[j], str(x[j]), str(data[i][j]), str(round(per_ret[i][j],2)), str(round(cum_per_ret[i][j],2)), str(round(per_finer[i][j],2))))
		f.write('\n\n')
		
	f.close()
	plt.show()
	return 0
