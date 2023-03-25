old_price = 4
new_price = 7
old_supply = 10
new_supply = 11


# percent change in price
price_change = (new_price - old_price) / old_price


# percent change in supply
supply_change = (new_supply - old_supply) / old_supply

e_number = supply_change/price_change

# elasticity
print(e_number)

if e_number>1:
    print("Supply is elastic")
elif e_number==1:
    print("Supply is unitary or proportional")
elif e_number<1:
    print("Supply is inelastic")
else:
    print("?")


