#The modulus (%) finds the remainder
#print(5%3) 

print(31%10) 

#Use the modulus in a loop to find factors

number = 12 

# Find all factors 
for test_factor in range(1,number+1): 
    if number%test_factor==0: 
        print(test_factor) 
        
#Reduce fractions to lowest terms

numerator = 12
denominator = 24
factor = 1

# Find greatest common factor 
for test_factor in range(1,denominator+1): 
    if numerator%test_factor==0 and denominator%test_factor==0:
        factor = test_factor 

# Divide out greatest common factor 
n = int(numerator/factor) 
d = int(denominator/factor) 

print("original: ", numerator, "/", denominator) 
print("reduced: ", n, "/", d) 

##You can add this code to the decimal-to-fraction code
# Get the decimal number to convert
digits = input("Enter a decimal number to convert: ") 

# Convert to fraction 
exponent = int(len(digits))-1 
n = float(digits) 
numerator = int(n * 10**exponent) 
denominator = 10**exponent 

# Reduce that fraction
factor = 1 
for test_factor in range(1,denominator+1): 
    if numerator%test_factor==0 and denominator%test_factor==0: 
        factor = test_factor 

# Divide out greatest common factor 
num = int(numerator/factor) 
den = int(denominator/factor) 

# Output 
print("The decimal is ", n) 
print("The fraction is ", num, "/", den)   

###Next level... factoring square roots

#import math

#print(math.sqrt(24)) 

import math

# number to factor
n = 12 

# This variable will change
max_factor = 1 

# The key ingredient
upper_limit = math.floor(math.sqrt(n)) + 1 

# Find square factors
for maybe_factor in range(1,upper_limit): 
    if n % (maybe_factor**2) == 0: 
        max_factor = maybe_factor 

# Results so far
print("n = ", n) 
print("Square rooted factor = ", max_factor) 
print("Square factor = ", max_factor**2) 
print("integer: ", n/(max_factor**2))      



     
     
