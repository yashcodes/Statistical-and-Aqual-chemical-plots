import numpy
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.tri as tri
import matplotlib.cm as cm

def ternary_plot(data_fn):

	reader = pd.read_csv(data_fn)
					   
	SQRT3 = numpy.sqrt(3)
	SQRT3OVER2 = SQRT3 / 2.

	def unzip(l):
		return zip(*l)

	def permute_point(p, permutation=None):
		if not permutation:
			return p
		return [p[int(permutation[i])] for i in range(len(p))]

	def project_point(p, permutation=None):
		permuted = permute_point(p, permutation=permutation)
		a = permuted[0]
		b = permuted[1]
		x = a + b/2.
		y = SQRT3OVER2 * b
		return numpy.array([x, y])

	def project_sequence(s, permutation=None):
		xs, ys = unzip([project_point(p, permutation=permutation) for p in s])
		return xs, ys

	data = []
	for i, (a, b, c) in reader.iterrows():
		a_ = a / (a + b + c)
		b_ = b / (a + b + c)
		c_ = c / (a + b + c)
		data.append((a_, b_, c_))

	xs, ys = project_sequence(data)
	vs = (1, 2, 3)

	fig = plt.figure(num=None, figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
	corners = numpy.array([[0, 0], [1, 0], [0.5,  numpy.sqrt(3) * 0.5 * 1]])
	triangle = tri.Triangulation(corners[:, 0], corners[:, 1])

	# creating the grid
	refiner = tri.UniformTriRefiner(triangle)
	trimesh = refiner.refine_triangulation(subdiv=4)

	#plotting the colorbar
	colormap = plt.cm.get_cmap('Reds')

	#plotting the mesh
	plt.triplot(trimesh, '', color='0.9', zorder = 1)

	#plotting the points
	plt.scatter(xs, ys, c=vs, s=100, zorder = 10, cmap=colormap)
	for i in range(len(xs)):
		plt.text(xs[i] + 0.001, ys[i] + 0.001, 'Samp-' + str(i))
	plt.tricontourf(xs,ys,triangle.triangles,vs)

	#plotting the axes
	plt.plot([corners[0][0], corners[1][0]], [corners[0][1], corners[1][1]], color='0.7', linestyle='-', linewidth=2)
	plt.plot([corners[0][0], corners[2][0]], [corners[0][1], corners[2][1]], color='0.7', linestyle='-', linewidth=2)
	plt.plot([corners[1][0], corners[2][0]], [corners[1][1], corners[2][1]], color='0.7', linestyle='-', linewidth=2)

	def plot_ticks(start, stop, tick, n):
	    r = numpy.linspace(0, 1, num = 10)
	    xs = start[0] * (1 - r) + stop[0] * r
	    xs = numpy.vstack((xs, xs + tick[0]))
	    ys = start[1] * (1 - r) + stop[1] * r
	    ys = numpy.vstack((ys, ys + tick[1]))
	    for i in range(0, len(xs.tolist()[1])):
	        x = xs.tolist()[1][i]
	        y = ys.tolist()[1][i]
	        plt.text(x, y, i, ha='center') 
	    plt.plot(xs, ys, 'k', lw=1, color='0.7')

	n = 10
	tick_size = 0.2
	margin = 0.1

	left = corners[0]
	right = corners[1]
	top = corners[2]

	# define vectors for ticks
	bottom_tick = tick_size * (right - top) / n
	right_tick = tick_size * (top - left) / n
	left_tick = tick_size * (left - right) / n

	# plot_ticks(left, right, bottom_tick, n)
	# plot_ticks(right, top, right_tick, n)
	# plot_ticks(left, top, left_tick, n)

	names = [reader[column].name for column in reader]

	plt.text(left[0] - 0.01, left[1], names[2], horizontalalignment = 'right', fontsize = 15, color = 'b')
	plt.text(right[0], right[1], names[0], horizontalalignment = 'left', fontsize = 15, color = 'b')
	plt.text(top[0], top[1], names[1], fontsize = 15, color = 'b')

	plt.colorbar(label="Sample density")
	#
	# plt.savefig('chart.png')
	plt.show()