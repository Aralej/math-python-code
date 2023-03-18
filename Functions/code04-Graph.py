#Basic blank graph
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
plt.show()

#Define dimensions of graph

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Dimensions
plt.axis([-10,10,-10,10]) 

plt.show()

#A better way to set dimensions

import matplotlib.pyplot as plt

xmin = -10
xmax = 10
ymin = -10
ymax = 20

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.show()

#Display axis lines

import matplotlib.pyplot as plt

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

plt.show()

#Plot one point

import matplotlib.pyplot as plt

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis


plt.plot([5],[4], 'ro')

plt.show()

#Plot several points as a function

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

##Graph and table of (x,y) values

import matplotlib.pyplot as plt

xmin = -10
xmax = 10
ymin = -10
ymax = 10

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

print("x \t y")
for x in range(xmin, xmax+1):
    y = 0.5*x + 1
    plt.plot([x],[y], 'ro')
    print(x,"\t",y)

plt.show()

