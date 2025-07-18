# Can contain only True/False


a = True # a and b are boolean var
b = False
print(type(a))

# but if you write code something like
# a = true then python interpreter will treat the 'true' as a varible and will find it in the code 

age = 17
is_adult = age >= 18
print(f"Are you adult: {is_adult}")


# bool is the subclass of int class
print(f"(True == 1): {True == 1}")
print(f"(False == 0): {False == 0}")

# Hence True corresponds to int value 1 and False corresponds to int value 0
print(f"(True + True): {True + True}")
print(f"(True + False + True + 8): {True + False + True + 8}")
print(f"True correspondes to int value: {int(True)}")
print(f"False correspondes to int value: {int(False)}")

# Beyond True and False Python treat values as Truthy and Falsy
# Truthy: Equavant to True
# Falsy: Equavant to Falsy

print(f"1 corresponds to boolean value: {bool(1)}")
print(f"0 corresponds to boolean value: {bool(0)}")

# Pyhton Falsy Values:
print(f"bool(0): {bool(0)}")
print(f"bool(0.0): {bool(0.0)}")
print(f"bool(''): {bool('')}")
print(f"bool([]): {bool([])}")
print(f"bool({{}}): {bool({})}")
print(f"bool(None): {bool(None)}")
print("--------------------------------")
# Python Truthy Values
print(f"bool(42): {bool(42)}")
print(f"bool(-1): {bool(-1)}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool([1, 2]): {bool([1, 2])}")

# is Every boolean an interger: Yes
# True --> 1
# False --> 1
print(f"isinstance(True, int): {isinstance(True, int)}")
# Are intergers a boolean: No
print(f"isinstance(1, bool): {isinstance(1, bool)}")

# Hence it is clear that every 'boolean' is an 'integer' but 'integers' are not 'boolean'

a = 10
print(f"{a}.bit_length(): {a.bit_length()}") # return the no. of bits in its binary representation

print(f"True.bit_length(): {True.bit_length()}")  # 1 bit
print(f"False.bit_length(): {False.bit_length()}") # 1

# Booleans are more memory efficient as requires one bit only