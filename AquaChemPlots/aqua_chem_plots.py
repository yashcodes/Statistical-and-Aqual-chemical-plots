from .ludwig_lang_plot import ludwig_lang_plot
from .mwl_plot import mwl_plot
from .time_plot import time_plot
from .stiff_plot import stiff_plot
from .wilcox_plot import wilcox_plot

def aqua_chem_plot(tool = None, data_fn = None, cation_data_fn = None , anion_data_fn = None, cations = None, anions = None):

	if tool < 1 or 5 < tool :
		raise Exception("Try again with correct tool number (from 1 to 5).")

	try:
		if tool == 1:
			ludwig_lang_plot(cation_data_fn, anion_data_fn, cations, anions)
			return "Ludwig-Langelier Plot"

		elif tool == 2:
			mwl_plot(data_fn)
			return "Meteoric Water Line (MWL) Plot"

		elif tool == 3:
			wilcox_plot(data_fn)
			return "Wilcox Diagram"

		elif tool == 4:
			stiff_plot(data_fn)
			return "Stiff Plot"
		elif tool == 5:
			time_plot(cation_data_fn, anion_data_fn)
			return "Time Plot"
	except:
		
		raise Exception("Data is not in coorect format.")


