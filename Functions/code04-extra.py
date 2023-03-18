#Loop through function inputs

import matplotlib.pyplot as plt

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

for x in range(10):
    y = 0.5*x + 1
    plt.plot([x],[y], 'ro')

plt.show()

#Use an array as inputs
import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 2*(xmax-xmin) 
x = np.linspace(xmin, xmax, points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

y = 2*x +1
plt.plot(x,y, 'pink')

plt.show()

##More ways to customize a graph
import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin, xmax, points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

ax.set_xlabel("x values")
ax.set_ylabel("y values")
ax.set_title("Some Graph")
ax.grid(True)

ax.set_xticks(np.arange(xmin, xmax, 1))
ax.set_yticks(np.arange(ymin, ymax, 1))

y = 2*x +1
plt.plot(x,y, label='y=2x+1')
plt.plot([4],[6], 'ro', label='point')
plt.plot(x,3*x, label='steeper line')
plt.legend()
plt.show()
