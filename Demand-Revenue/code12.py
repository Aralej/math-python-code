#Selling shirts

price = 10
demand = 50 - 2*price 
revenue = price*demand 
total_cost = 4*demand 
profit = revenue - total_cost 

print("price: ", price)
print("demand: ", demand)
print("revenue: ", revenue)
print("total cost: ", total_cost)
print("profit ", profit)


#Grpah example
import matplotlib.pyplot as plt
import numpy as np

# price = x
# demand = y

price_1 = 2
demand_1 = 46
price_2 = 10
demand_2 = 30
m = (demand_2 - demand_1)/(price_2 - price_1)
b = demand_1 - m*price_1
# This becomes a y = mx + b equation 

xmin = 0
xmax = 50
ymin = 0
ymax = 320
points = 10*(xmax-xmin)
x = np.linspace(xmin,xmax,points)

fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis

plt.xlabel("Price")
plt.title("Financial Algebra")

# line 1
demand = m*x + b
#plt.ylabel("Demand") 
#plt.plot(x, demand) 

# line 2
revenue = x*demand
plt.plot(x, revenue) 
plt.ylabel("Revenue")

plt.show()

