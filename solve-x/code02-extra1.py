

import sympy 
from sympy import symbols 
from sympy.solvers import solve 

x = symbols('x') 

eq = input('Enter equation: 0 = ')

solution = solve(eq,x)

# pick up one solution
#print("x = ", solution[0]) # first solution

# show every equation solution
for s in solution:
    print("x = ", s)

