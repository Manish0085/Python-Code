# Tuple unpacking allows you to assign tuple elements to individual variables in a single operation


t = 1, 2, 3   # Tuple
print(f"tuple t: {t}")
print(f"type(t): {type(t)}\n")
a, b, c = t
print(f"a: {a}, b: {b}, c: {c}")
print(f"type(a): {type(a)}, type(b): {type(b)}, type(c): {type(c)}\n")


# Python does this by matching the structure(number of element/items) on both the sides of the assignment operator

# a, b = 1, 2, 3  # ValueError: too many values to unpack (expected 2)
# a, b = t  # ValueError: too many values to unpack (expected 2)

# but you can do these by following:
a, *b = 1, 2, 3, 4
# What python does to assign above values
# a = 1
# b = [1, 2, 3]
print(f"a: {a}")
print(f"type(a): {type(a)}")
print(f"b: {b}")
print(f"type(b): {type(b)}\n")


a, *b, c = 1, 2, 3, 4, 5, 6, 7
print(f"a: {a}")
print(f"type(a): {type(a)}")
print(f"b: {b}")
print(f"type(b): {type(b)}")
print(f"c: {c}")
print(f"type(c): {type(c)}\n")


# you can unpack any of the iterable
a, *b, c = [1, 2, 3, 4, 5, 6, 7]  # unpacking a list
print(f"a: {a}")
print(f"type(a): {type(a)}")
print(f"b: {b}")
print(f"type(b): {type(b)}")
print(f"c: {c}")
print(f"type(c): {type(c)}\n")


# unpacking of string
a, *b, c, d = "education"
print(f"a: {a}")
print(f"type(a): {type(a)}")
print(f"b: {b}")
print(f"type(b): {type(b)}")
print(f"c: {c}")
print(f"type(c): {type(c)}")
print(f"d: {d}")
print(f"type(d): {type(d)}\n")


# exmpale
data = ("Jhon", 30, "Manager", 50000, "New York")
name, age, designation, salary, name = data
print(name)  # New York


# unpacking of nested tuples
(a, b), (c, d), (e, f) = ((1, 2), (3, 4), (4,5 ))


# You can use '_' if you want to ignore the name of varible anywhere in python 



