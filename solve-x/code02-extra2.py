# solving in other ways
from sympy import *


var('x y') 

# First equation set equal to zero, ready to solve
first = 2*x - y


# Sympy syntax for equation equal to zero, ready to factor
eq1 = Eq(first,0) 

# Sympy solve for x
sol = solve(eq1,x) 

# Show factored results
print("x = ", sol[0])
