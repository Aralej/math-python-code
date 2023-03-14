# Factoring
import sympy 
from sympy import * 

var('x y') 

# Equation set equal to zero, ready to solve
#eq = x**2-4
eq = x**3 - 2*x**2 - 5*x + 6 

sympy.factor(eq)
