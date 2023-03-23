#matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np

# Define the graphing function
def f(m, b, zoom):
    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom
    points = 10*xmax-xmin
    x = np.linspace(xmin, xmax, points)

    plt.axis([xmin,xmax,ymin,ymax]) # window size
    plt.plot([xmin,xmax],[0,0],'black') # black x axis
    plt.plot([0,0],[ymin,ymax], 'black') # black y axis
    
    # Line 1
    y1 = 3*x**2 - 4
    
    # Line 2
    plt.plot(x, y1)
    plt.show()
    # plt.fill_between(x, y3, y2, facecolor='blue')

# Set up the sliders
interactive_plot = interactive(f, m=(-9, 9), b=(-9, 9), zoom=(1,100))
interactive_plot


