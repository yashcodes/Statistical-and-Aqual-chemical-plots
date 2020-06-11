from .freq_hist import plot_histograms_multi_fig, plot_histograms_sing_fig
from .normalize import normalize
from .gen_random import rand
from .gen_normal_random import normal_rand
from .seive_diagram import seive_diagram
from .standardization import standardization
from .ternary_plot import ternary_plot
from .stat_report import stat_report 
from .scattergram import linear_regression, poly_regression


def statistical_tool(tool = None, data_fn = None, fig = 1, fit = 'lin', filter = False, new_min = None, new_max = None, decimal = 2,  bins_list = None, log_scale = False, nums = None, mean = None, std_dev = None, degree = 2):
	if tool < 1 or 9 < tool :
		raise Exception("Try again with correct tool number (from 1 to 11).")

	try:
		if tool == 1:
			if fig == 1:
				plot_histograms_sing_fig(data_fn, bins_list = bins_list, log_scale = log_scale)
				return "Histogram"
			else:
				plot_histograms_multi_fig(data_fn, bins_list = bins_list, log_scale = log_scale)
				return "Histogram"

		elif tool == 2:
			rand(nums, new_min, new_max, decimal = decimal)
			return "Random Numbers"

		elif tool == 3:
			normal_rand(nums, mean, std_dev, decimal = decimal)
			return "Normal distributed Random numbers"

		elif tool == 4:
			normalize(data_fn, new_min = new_min, new_max = new_max, decimal = decimal)
			return "Normalization"

		elif tool == 5:
			seive_diagram(data_fn)
			return "Seive Diagram"

		elif tool == 6:
			standardization(data_fn, decimal = decimal)
			return "Standardization"

		elif tool == 7:
			ternary_plot(data_fn)
			return "Ternary Plot"

		elif tool == 8:
			stat_report(data_fn, filter = filter, new_min = new_min, new_max = new_max)
			return "Statistic Report"

		elif tool == 9:
			if fit == 'lin':
				linear_regression(data_fn)
				return "Scattergram with fitted Linear Regression"
			elif fit == 'poly':
				poly_regression(data_fn, degree = degree)
				return "Scattergram with fitted Ploynomial Regression of degree " + str(degree)
	except:
		
		raise Exception("Given data is not in correct format.")

	return 
