import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
from matplotlib.patches import Arc

# First Sampling Method #
# We will use the first sampling method to calculate the probability of a chord being longer than a side of the equilateral triangle.
# Sampling the angle of chord.
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
theta_1 = np.random.uniform(0,2*math.pi, samples)
theta_2 = np.random.uniform(0,2*math.pi, samples)
point_pairs = [((radius*np.cos(theta_1[i]), radius*np.sin(theta_1[i])),(radius*np.cos(theta_2[i]), radius*np.sin(theta_2[i]))) for i in range(samples)]
length = radius*2*np.sin(abs(theta_1-theta_2)/2)
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



##----------------------------------------------------------------------------------------------------------------------------##
##----------------------------------------------------------------------------------------------------------------------------##
## PLOTTING THE ANIMATION



# Create empty plot
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize=(7, 7))
ax1.set_title("Visual of Chords as they are chosen", fontsize=8)
ax2.set_title("Number of Samples plotted against probability", fontsize=8)
ax3.set_title("No of successes vs failures ", fontsize=8)
ax4.set_title("Sampling of points on the perimeter of a circle", fontsize=8)


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

# FIG4
circle=plt.Circle((0,0), radius, color="black", fill=False)
theta_1=np.random.rand()*2*math.pi
theta_2=np.random.rand()*2*math.pi
x_1=radius*math.cos(theta_1)
y_1=radius*math.sin(theta_1)
x_2=radius*math.cos(theta_2)
y_2=radius*math.sin(theta_2)
chord=plt.Line2D((x_1,x_2), (y_1,y_2), lw=2.5, color="red")
line_1=plt.Line2D((0,x_1), (0,y_1), lw=1.5, color="blue")
line_2=plt.Line2D((0,x_2), (0,y_2), lw=1.5, color="blue")
x_axis=plt.Line2D((-radius, radius), (0,0), lw=1.5, color="green")
ax4.add_artist(circle)
ax4.add_artist(chord)
ax4.add_artist(line_1)
ax4.add_artist(line_2)
ax4.add_artist(x_axis)

# Add annotations for theta_1 and theta_2
# Annotate angle 1
ax4.annotate(f'{theta_1*57:.2f}°', xy=(x_1, y_1), xytext=(x_1 + 0.5, y_1 + 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05, linewidth=0.5, width=0.1, headwidth=8))

# Annotate angle 2
ax4.annotate(f'{theta_2*57:.2f}°', xy=(x_2, y_2), xytext=(x_2 + 0.5, y_2 + 0.5),
           arrowprops=dict(facecolor='black', shrink=0.05, linewidth=0.5, width=0.1, headwidth=8))
# Add text annotations for angles
ax4.text(x_1, y_1, fr'$\theta_1$', ha='center', va='center', color='blue')
ax4.text(x_2, y_2, fr'$\theta_2$', ha='center', va='center', color='blue')



ax4.set_xlim(-radius-1, radius+1)
ax4.set_ylim(-radius-1, radius+1)
ax4.grid(color='lightgrey', linestyle='-', linewidth=0.5)
ans = right/(right+wrong)
legend_elements = [Line2D([0], [0], color='#000000', lw=0, label='Probability Expected = 0.33'),
                   Line2D([0], [0], color='#000000', lw=0, label=f'Probability Obtained (# of Samples = {samples}) = {ans:.4f}'),]
fig.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, 0), ncol=2)
legend_elements = [Line2D([0], [0], color='#000000', lw=0, label='SAMPLING ANGLE OF CHORD'),]

plt.show()