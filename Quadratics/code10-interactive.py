#Sliders to show how a, b, and c affect the graph

#matplotlib inline
from ipywidgets import interactive
import matplotlib.pyplot as plt
import numpy as np
import math

# All graphing happens in this function
def f(a,b,c):
    xmin = -10
    xmax = 10
    ymin = -10
    ymax = 10
    points = 10*(xmax-xmin)
    x = np.linspace(xmin,xmax,points)

    plt.axis([xmin,xmax,ymin,ymax]) # window size
    plt.plot([xmin,xmax],[0,0],'b') # x axis
    plt.plot([0,0],[ymin,ymax], 'b') # y axis

    # Parabola
    y1 = a*x**2 + b*x + c 
    plt.plot(x, y1) 

    # Vertex
    vx = -b/(2*a) 
    vy = a*(vx**2) + b*vx + c 
    plt.plot([vx],[vy], 'ro') 

    # Roots
    d = b**2 - 4*a*c 
    if d>=0: 
        root_1 = (-b + math.sqrt(d))/(2*a) 
        root_2 = (-b - math.sqrt(d))/(2*a) 
        plt.plot([root_1, root_2],[0,0], 'go') 
    
    # Set the equation as the title
    sa = str(a)
    sb = str(b)
    sc = str(c)
    h1 = "y = ", sa, "x**2 + ", sb, "x + ", sc
    h2 = ""
    for w in h1:
        h2 = h2 + w

    plt.title(h2)
    plt.show()
    
# Interactive creates sliders for a, b, and c values
interactive_plot = interactive(f, a=(1, 9), b=(-9,9), c=(-9,9))
interactive_plot

