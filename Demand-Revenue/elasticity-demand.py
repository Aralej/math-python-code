old_demand = 5
new_demand = 6
old_price = 11
new_price = 10

# percent change in price
price_change = (new_price - old_price) / old_price


# percent change in demand
demand_change = (new_demand - old_demand) / old_demand

e_number = demand_change/price_change  #the price elasticity of demand

# elasticity
print(e_number)

if e_number>1:
    print("Demand is elastic")
elif e_number==1:
    print("Demand is unitary or proportional")
elif e_number<1:
    print("Demand is inelastic")
else:
    print("?")
