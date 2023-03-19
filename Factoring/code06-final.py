##Using Sympy to make this look nice
import math
import sympy
from sympy import symbols

n = 24 

# Use these variables
upper_limit = math.floor(math.sqrt(n)) + 1 
max_factor = 1 
other_factor = 1 
square_root = 1 

# Slightly different variable strategy
for maybe_factor in range(1, upper_limit): 
    if n % (maybe_factor**2) == 0: 
        max_factor = maybe_factor**2 

# Divide out the greatest square factor
other_factor = n/max_factor 

# Output variables
square_root = int(math.sqrt(max_factor)) 
other_factor = int(other_factor) 
output = square_root*sympy.sqrt(other_factor) 

# Sympy output without print statement - must be last line
print(output) 

