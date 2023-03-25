import matplotlib.pyplot as plt

old_demand_x = 1
new_demand_x = 12
old_price_y = 14
new_price_y = 3
old_supply_x = 11
new_supply_x = 1

# For the graph
xmin = 0
xmax = 15
ymin = 0
ymax = 15


# Basic setup for the graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis
plt.xlabel("Quantity")
plt.ylabel("Price")
plt.title("Green=Supply, Red=Demand")

# Plot the demand function as a red line
plt.plot([old_demand_x,new_demand_x],[old_price_y,new_price_y],'r')

# Plot the supply function as a green line
plt.plot([old_supply_x,new_supply_x],[old_price_y,new_price_y],'g')

plt.show()
