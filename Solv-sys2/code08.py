#implest way to solve a system of equations. Set each equation equal to zero

from sympy import *

x,y = symbols('x y')

# Equations set equal to zero
first = 2*x + y - 1 
second = x - 2*y + 7 

# The solution
print(linsolve([first, second], (x, y))) 


#Nicer looking output

from sympy import *

x,y = symbols('x y')

first = 2*x + y - 1 
second = x - 2*y + 7 


# parse finite set answer as coordinate pair
solution = linsolve([first, second], (x, y)) 
x_solution = solution.args[0][0] 
y_solution = solution.args[0][1] 

# Print a coordinate pair
print("(", x_solution, ",", y_solution, ")") 

