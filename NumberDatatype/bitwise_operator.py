# Bitwise Operator in python

x = 10 # 1010 in binary 
y = 6  # 0110 in binary 
       # --------------
       # 0010 in binary
       # 2 in decimal
# BITWISE AND &
bitwisw_and = x & y
print(f"BITWISE AND of {x} ({bin(x)} in binary) and {y} ({bin(y)} in binary) is {bitwisw_and} ({bin(bitwisw_and)} in binary)")



# BITWISE OR |
# output ----------------
        # 1110 in binary
        # 14 in decimal
bitwisw_or = x | y
print(f"BITWISE OR of {x} ({bin(x)} in binary) and {y} ({bin(y)} in binary) is {bitwisw_or} ({bin(bitwisw_or)} in binary)")


# BITWISE XOR ^
# output ----------------
        # 1100 in binary
        # 12 in decimal
bitwisw_xor = x ^ y
print(f"BITWISE XOR of {x} ({bin(x)} in binary) and {y} ({bin(y)} in binary) is {bitwisw_xor} ({bin(bitwisw_xor)} in binary)")


#BITWISE NOT ~
bitwisw_not = ~x
# x --> 10
# binary of x --> 00001010 
# inverts the bit of x --> 1111 0101 (if the Least significat bit is zero, it mean the number is negative)
# how to calculate that negative number
# --------------------------------------
# Step 1: inverts the bit again (called 1's compliment)
# ------
#         1111 0101 --> 0000 1010
# Step 2: add the result in the above result
# ------- 
#         0000 1010 + 00000001  --> 0000 1011 which is 11 in decimal but negative
print(f"BITWISE NOT of {x} ({bin(x)} in binary) is {bitwisw_not} ({bin(bitwisw_not)} in binary) ")


# Left shift
left_shift = x << 1
print(f"{x} ({bin(x)} in binary) << 1 = {left_shift} ({bin(left_shift)} in binary)")


# Right shift
right_shift = x >> 1
print(f"{x} ({bin(x)} in binary) >> 1 = {right_shift} ({bin(right_shift)} in binary)")



# Questions

# '//' returns largest integer less than or equal to the exact division result
print(f"10 // 3 = {10 // 3}")      # output: 3 
print(f"10.0 // 3 = {10.0 // 3}")  # output: 3.0 beacuse we made one operand float that's why the result will be float
print(f"-10 // 3 = {-10 // 3}")    # output: -4 because the exact result is -3.33333 and the less than or equal to it is -4
print(f"10 // -3 = {10 // -3}")    # output: -4 reason same as the above


# Assignment opeartor

x = 1
name = "Vipul" # here "Vipul" is literal
# 5 = x Not valid
# LHS = RHS
# LHS must always be a variable
# RHS must a valu(literal) or a expression itself which produces a value

# Question: swap the value 

inp = input("Enter any value: ")
print(F"Default type of value given by user as input = {type(inp)}")
# by default the type of the value give by user is string that's why we use int() to accept the integer type value by python interpreter only



x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
print(f"type of x = {type(x)} and type of y = {type(y)}")
print(f"before swaping x = {x} and y = {y}")

# General way 
# temp = x
# x = y
# y = temp

# Using flexibility given by python:
x, y = y, x
print(f"before swaping x = {x} and y = {y}")


salary = 11
salary **= 2 # same as salary = salary ** 2
print(salary)


msg = "Hello"
msg += "World"   # mag = msg + "World"
print(msg)