# Floating point number in Python

# float has typipcally 15-17 significant digit precision
salary = 1.56
z = -0.323
x = -.2332
print(x)
a = 4.0
print(type(a))
b = 7 / 2
print(b)
c = float(7)
print(c)
d = float("7")
print(d)
# d = float("7a") Not valid, throw error 

e = int(9.2)
print(e)

result = 0.1 + 0.2  # Output: 0.30000000000000004 because unpredicatable precision  
print(f"0.1 + 0.2 = {result}")

result = 0.5 + 0.125
print(f"0.5 + 0.125 = {result}")  # 0.625
# those decimal number whose Denominator are in the from of pow(2) can be stored in the computer system easily and completely

# if we have big numbers then we use pow(10) for example:
electron_mass = 9.11e-31   # 9.11 * 10 ^ (-31)
print(f"Mass of Electron is {electron_mass}")
# e means exponent of 10 (e-30 = 10 ^ (-31))

result1 = 5e3 * 2e3 
# 5e3 = 5 * 10^3 = 5 * 1000 = 5000
# 2e3 = 2 * 10^3 = 2 * 1000 = 2000
# 5e3 * 2e3  = 10000000.0
print(f"5e3 * 2e3  = {result1}")

a = 1500.0
b = 1.5e3
print(f"{a} == {b}: {a == b}") # True

very_large_int = 10000000000000000
very_large_float = 10000000000000000.0
print(f"very_large_int: {very_large_int}\nvery_large_float: {very_large_float}")

very_small_float = 0.0000000000000001
print(f"very_small_float: {very_small_float}")

pos_infinity = float('inf')
print(f"Positive infinity number: {pos_infinity}")

neg_infinity = float('-inf')
print(f"Negative infinity number: {neg_infinity}")



pi = 3.14159265359
print(f"value of pi: {pi:.4f}")


a = 0.3
b = 0.1 + 0.2
print(f"{a} == (0.1 + 0.2): {a == b}")


 