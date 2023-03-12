# converts string input (including fractions) to float
def string_frac(in_string):
    if "/" in in_string:
        nd = in_string.split("/")
        n = float(nd[0])
        d = float(nd[1])
        ans = n/d
        return ans
    else:
        ans = float(in_string)
        return ans


# Proportions - unknown numerator
def proportions_n():
    import random
    # Uses string_frac() function
    n1 = random.randint(1,21)
    d1 = random.randint(1,21)
    n2 = "x"
    d2 = random.randint(1,21)
    print(n1, "\t\t", n2)
    print("--- \t = \t ---")
    print(d1, "\t\t", d2)
    print(" ")
    ans_in = input("x = ")
    answer = d2*n1/d1
    if string_frac(ans_in)==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


# Proportions - unknown denominator
def proportions_d():
    import random
    # Uses string_frac() function
    n1 = random.randint(1,21)
    d1 = random.randint(1,21)
    n2 = random.randint(1,21)
    d2 = "x"
    print(n1, "\t\t", n2)
    print("--- \t = \t ---")
    print(d1, "\t\t", d2)
    print(" ")
    ans_in = input("x = ")
    answer = d1*n2/n1
    if string_frac(ans_in)==answer:
        print("Correct! \n")
    else:
        print("Try again")
        print("The correct answer is ", answer, "\n")


# test loop
for a in range(2):
    proportions_n()
    proportions_d()
    print(" ")


