x1 = 1
y1 = 7
x2 = 2
y2 = 10

slope = (y2 - y1) / (x2 - x1)

print("slope = ", slope)

#Next, developing equations...

x1 = 632 #1
y1 = 84 #7
x2 = 1800 #2
y2 = 8 #10

# The slope is "m"
m = (y2 - y1) / (x2 - x1)

# The y intercept is "b"
b = y1 - m*x1

# The full equation
print("y = ", m, "x + ", b)

####Also display the graph
import matplotlib.pyplot as plt

x1 = 2
y1 = 3
x2 = 6
y2 = 8

# Develop the equation y = mx + b
m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1
print("y = ", m, "x + ", b)

# For the graph
xmin = -10
xmax = 10
ymin = -10
ymax = 10

# For the line on the graph
y3 = m*xmin + b 
y4 = m*xmax + b 

# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

# Plot the linear function as a red line
plt.plot([xmin,xmax],[y3,y4],'r')

plt.show()
