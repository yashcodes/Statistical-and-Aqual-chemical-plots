"""
Generate text file 'univar_stat_report.txt'
"""
import os
import pandas as pd
import math
import statistics as stat

def stat_report(data_fn, filter = False, new_min = None, new_max = None):
	
	reader = pd.read_csv(data_fn)

	if filter:
		del_data = []
		data = []
		for value in reader.iloc[:, 0].values:
			if new_min <= value <= new_max:
				data.append(value)
			else:
				del_data.append(value)
	else:
		data = reader.iloc[:, 0].values

	pop = len(data)
	min_val = min(data)
	max_val = max(data)
	mean = stat.mean(data)
	std_dev = stat.stdev(data)
	abs_dev = stat.mean(abs(data - mean))
	median = stat.median(data)
	std_error = std_dev / math.sqrt(pop)
	total = sum(data)
	sqrt_sum = math.sqrt(total)
	sum_squared = total * total
	var = std_dev * std_dev

	stat_cutoff_data1 = []
	m_plus_std = mean + std_dev
	mid = int(pop/2)
	data.sort()
	k = mid

	while 1:
		temp = []
		for i in range(k, pop):
			if mean <= data[i]:
				if data[i] < m_plus_std:
					temp.append(data[i])
				else:
					k = i
					m_plus_std = m_plus_std + std_dev
					stat_cutoff_data1.append(temp)
					break
			else:
				k = i + 1 
				break	
		if max_val < m_plus_std:
			break
	
	k = mid	
	m_min_std = mean - std_dev
	stat_cutoff_data2 = []

	while 1:
		temp = []
		for i in range(k, -1, -1):
			if data[i] <= mean:
				if m_min_std <= data[i]:
					temp.append(data[i])
				else:
					k = i
					m_min_std = m_min_std - std_dev
					stat_cutoff_data2.append(temp)
					break
			else:
				k = i - 1 
				break	
		if m_min_std < min_val:
			break

	f = open("univar_stat_report.txt", "w+")
	f.write('Univariate Statistics\n\n')
	f.write('    Population......................... %s\n' %(str(pop)))
	f.write('    Minimum Value...................... %s\n' %(str(min_val)))
	f.write('    Maximum Value...................... %s\n' %(str(max_val)))
	f.write('    Range.............................. %s\n' %(str(max_val - min_val)))
	f.write('    Mean............................... %s\n' %(str(mean)))
	f.write('    Standard Deviation................. %s\n' %(str(std_dev)))
	f.write('    Average Deviation.................. %s\n' %(str(abs_dev)))
	f.write('    Standard Error..................... %s\n' %(str(std_error)))
	f.write('    Median............................. %s\n' %(str(median)))
	f.write('    Sum................................ %s\n' %(str(total)))
	f.write('    Square root of Sum................. %s\n' %(str(sqrt_sum)))
	f.write('    Sum Squared........................ %s\n' %(str(sum_squared)))
	f.write('    Variance........................... %s\n\n' %(str(var)))
	f.write('    Statistic Cutoff Data : \n')
	f.write('             Data between "Mean and Mean + 1Std" => %s\n' %(str(stat_cutoff_data1[0])))
	concat_list = stat_cutoff_data1[0]
	for i in range(1, len(stat_cutoff_data1)):
		concat_list.extend(stat_cutoff_data1[i])
		f.write('             Data between "Mean and Mean + %sStd" => %s\n' %(str(i+1), str(concat_list)))
	
	f.write('             Data between "Mean - 1Std and Mean" => %s\n' %(str(stat_cutoff_data2[0])))
	concat_list = stat_cutoff_data2[0]
	for i in range(1, len(stat_cutoff_data2)):
		concat_list.extend(stat_cutoff_data2[i])
		f.write('             Data between "Mean - %sStd and Mean" => %s\n' %(str(i+1), str(concat_list)))

	if filter:
		f.write('  Deleted Population\n')
		f.write(str(del_data))

	f.close()

	return 