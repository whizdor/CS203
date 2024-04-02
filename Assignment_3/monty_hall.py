import math
import numpy as np
import math
import seaborn as sns
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
from matplotlib.patches import Arc
import itertools
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from numpy.random import randn
from scipy import array, newaxis
import sys

def monty_hall_switching(trials, num_doors, k):
	permutation = list([1]*k + [0]*(num_doors-k))
	for i in range(trials):
		np.random.shuffle(permutation)
		first_pick = np.random.randint(0, num_doors)
		host_can_open = [i for i, x in enumerate(permutation) if x == 0 and i != first_pick]
		host_opens = np.random.choice(host_can_open)
		second_picks = [i for i in range(num_doors) if i != first_pick and i != host_opens]
		second_pick = np.random.choice(second_picks)
		if(permutation[second_pick] == 1):
			k += 1
	return(k/trials)

def monty_hall_not_switching(trials, num_doors, k):
	permutation = list([1]*k + [0]*(num_doors-k))
	for i in range(trials):
		np.random.shuffle(permutation)
		first_pick = np.random.randint(0, num_doors)
		host_can_open = [i for i, x in enumerate(permutation) if x == 0 and i != first_pick]
		host_opens = np.random.choice(host_can_open)
		second_pick = first_pick
		if(permutation[second_pick] == 1):
			k += 1
	return(k/trials)

def compute():
	for n in range(3,1000):
		for k in range(1,n-1):
			probability_switching=monty_hall_switching(10000, n, k)
			probability_not_switching=monty_hall_not_switching(10000, n, k)
			points.append([n, k, probability_switching/probability_not_switching])
			with open('monty_hall_results.csv', 'w') as file:
				for point in points:
					file.write(f"{point[0]}, {point[1]}, {point[2]}\n")


# Graph Plotting Starts Here

fig, (ax1,ax2) = plt.subplots(1,2, figsize=(16, 5), subplot_kw={'projection': '3d'})
ax1.set_title("Surface Plot of Probability Ratio", fontsize=8)
ax2.set_title("Scatter Plot of Points", fontsize=8)

# Getting the points from the file
points = []
with open('monty_hall_results.csv') as file:
	lines = file.readlines()
	for line in lines:
		points.append([float(x) for x in line.strip().split(',')])
points = np.array(points)

# Graph 1
X=points[0:300,0]
Y=points[0:300,1]
Z=points[0:300,2]
surf = ax1.plot_trisurf(X, Y, Z, cmap=cm.jet, linewidth=0)
fig.colorbar(surf)
fig.tight_layout()
ax1.xaxis.set_major_locator(MaxNLocator(5))
ax1.set_xlabel('Number of Doors')
ax1.set_ylabel('Number of Cars')
ax1.set_zlabel('Probability Ratio')
ax1.yaxis.set_major_locator(MaxNLocator(6))
ax1.zaxis.set_major_locator(MaxNLocator(5))


# Graph 2
ax2.set_xlim([3,240])
ax2.set_ylim([3,240])
ax2.set_zlim([0,3])
ax2.set_xlabel('Number of Doors')
ax2.set_ylabel('Number of Cars')
ax2.set_zlabel('Probability Ratio')
i = 0
for n in range(3, 241):
	ax2.scatter(points[i:i+n-1, 0], points[i:i+n-1, 1], points[i:i+n-1, 2], color='r', marker='o', s=0.01)
	plt.draw()
	plt.pause(.00000001)
	i = i + n - 1
plt.show()
