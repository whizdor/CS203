import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D

# Third Sampling Method #
# We will use the second sampling method to calculate the probability of a chord being longer than a side of the equilateral triangle.
# Sampling Mid Point of the Chord
radius = np.random.randint(10, size=1)[0]
right = 0
wrong = 0
trial_no = []
probability = []
right_list = []
wrong_list = []
status = []

#Number of samples taken 
samples = 15000
x = []
y = []

for i in range(samples):
    temp_x = (np.random.rand()-0.5)*2*radius
    temp_y = (np.random.rand()-0.5)*2*radius
    while(temp_x**2 + temp_y**2 > radius**2):
        temp_x = (np.random.rand()-0.5)*2*radius
        temp_y = (np.random.rand()-0.5)*2*radius
    x.append(temp_x)
    y.append(temp_y)

theta_1 = np.random.uniform(0,2*math.pi, samples)
center = np.sqrt(np.square(x) + np.square(y))
x_1 = (center*np.cos(theta_1) + np.sqrt(np.square(radius) - np.square(center))*np.sin(theta_1))
y_1 = (center*np.sin(theta_1) - np.sqrt(np.square(radius) - np.square(center))*np.cos(theta_1))
x_2 = (center*np.cos(theta_1) - np.sqrt(np.square(radius) - np.square(center))*np.sin(theta_1))
y_2 = (center*np.sin(theta_1) + np.sqrt(np.square(radius) - np.square(center))*np.cos(theta_1))
point_pairs = [((x_1[i], y_1[i]),(x_2[i], y_2[i])) for i in range(samples)]

length = np.sqrt((radius**2 - np.square(x) - np.square(y)))*2
for i in range(samples):
    if length[i] > math.sqrt(3)*radius:
        right+=1
        status.append(1)
    else:
        wrong+=1
        status.append(0)
    if(i>10):
        trial_no.append(i+1)
        probability.append(right/(right+wrong))
        right_list.append(right)
        wrong_list.append(wrong)

ans = right/(right+wrong)
print(ans)
##----------------------------------------------------------------------------------------------------------------------------##
##----------------------------------------------------------------------------------------------------------------------------##
## PLOTTING THE ANIMATION



# Create empty plot
fig, (ax1,ax2,ax3) = plt.subplots(1,3, figsize=(15, 5))
ax1.set_title("Visual of Chords as they are chosen", fontsize=8)
ax2.set_title("Number of Samples plotted against probability", fontsize=8)
ax3.set_title("No of successes vs failures ", fontsize=8)


def equilateral_triangle( radius):
    height = length * np.sqrt(3) / 2
    vertices = [
        (0, radius), # Top vertex
        (radius*np.sqrt(3)/2, -radius/2), # Bottom right vertex
        (-radius*np.sqrt(3)/2, -radius/2) # Bottom left vertex
    ]
    return vertices

#FIG 1
# Initialize empty line segments
segments = []
# Initialization function: plot the background of each frame
def init_plot1():
    coordinate=radius+1
    line, = ax1.plot([], [], linewidth=0.5)  
    ax1.axhline(0, color='grey', linewidth=0.5)
    ax1.axvline(0, color='grey', linewidth=0.5)
    ax1.set_aspect('equal', adjustable='box')
    ax1.spines['left'].set_position('zero')
    ax1.spines['bottom'].set_position('zero') 
    ax1.spines['right'].set_position('zero')
    ax1.spines['top'].set_position('zero') 
    ax1.xaxis.set_ticks_position('bottom')
    ax1.yaxis.set_ticks_position('left')
    ax1.grid(color='lightgrey', linestyle='-', linewidth=0.5)
    ax1.set_xlim(-coordinate,coordinate)
    ax1.set_ylim(-coordinate,coordinate)
    ax1.set_xticks([x for x in range(-coordinate,coordinate+1) if x != 0])
    ax1.set_yticks([y for y in range(-coordinate,coordinate+1) if y != 0])
    circle = plt.Circle((0, 0),radius, color='k', fill=False, linewidth=2,  zorder=2)
    vertices = equilateral_triangle(radius)
    triangle = plt.Polygon(vertices, closed=True, edgecolor='black', facecolor='none', linewidth=2,  zorder=2)
    ax1.add_patch(triangle)
    ax1.add_artist(circle)
    return line,
# Animation function: update the plot with each frame
def animate_plot1(i):
    if i > 0:
        # Extract coordinates from the i-th pair
        (x_start, y_start), (x_end, y_end) = point_pairs[i-1]
        p = status[i-1]
        if(p ==1):
            segment, = ax1.plot([x_start, x_end], [y_start, y_end], linewidth=0.5, color='b',zorder=0,alpha=0.5)
        else:
            segment, = ax1.plot([x_start, x_end], [y_start, y_end], linewidth=0.5, color='r',zorder=0,alpha=0.5)
        segments.append(segment)
    return segments
# Create animation
anim = FuncAnimation(fig, animate_plot1, init_func=init_plot1, frames=len(point_pairs)+1, interval=2, blit=True)

#FIG2
ax2.plot(trial_no, probability)
ax2.spines['top'].set_linewidth(1)      # Top border
ax2.spines['right'].set_linewidth(1)    # Right border
ax2.spines['bottom'].set_linewidth(1)   # Bottom border
ax2.spines['left'].set_linewidth(1)     # Left border


#FIG3
ax3.set_ylim(0, samples)  # Setting y-axis limits for the new plot
palette = list(reversed(sns.color_palette("seismic", 2).as_hex()))
ax3.bar(["length>side", "length<=side"], [right, wrong], color=palette)

ans = right/(right+wrong)
legend_elements = [Line2D([0], [0], color='#000000', lw=0, label='Probability Expected = 0.25'),
                   Line2D([0], [0], color='#000000', lw=0, label=f'Probability Obtained (# of Samples = {samples}) = {ans:.4f}'),]
fig.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, 0), ncol=2)
plt.show()