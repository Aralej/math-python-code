#Notes and work
#1500 = 10x + 500
#0 = 10x - 1000

#Solve an equation

import sympy 
from sympy import symbols 
from sympy.solvers import solve 

x = symbols('x') 

# Put the equation here
eq = 10*x - 1000

solution = solve(eq,x)
print("x = ", solution[0])

#Graph the solution
import matplotlib.pyplot as plt
import numpy as np

x1 = 0
y1 = 0
x2 = 40
y2 = 13

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1
print("y = ", m, "x + ", b)

# For the graph
xmin = 0
xmax = 100
ymin = 0
ymax = 50

# For the line on the graph
y3 = m*xmin + b 
y4 = m*xmax + b 

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Add details to the graph
ax.set_xlabel("thousands")
ax.set_ylabel("tons")
ax.grid(True)
#ax.set_xticks(np.arange(xmin, xmax, 2))
#ax.set_yticks(np.arange(ymin, ymax, 1)) #2 


# Plot the linear function as a red line
plt.plot([xmin,xmax],[y3,y4],'r')

plt.show()

