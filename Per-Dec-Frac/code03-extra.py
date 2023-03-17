
from sympy import *
import math

# Identify all variables
var('a b c d x') 

# Left and right sides of the equal sign
left = 0
right = a*x**2 + b*x + c

# Variable to solve for
variable = x

# Sympy equation left = right
eq1 = Eq(left,right) 

# Sympy solve for that variable
sol = solve(eq1,variable) 

# Show factored results
for s in sol:
    print(variable, " = ", s)

