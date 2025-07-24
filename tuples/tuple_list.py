# Key differences between tuple and list

# 1. Tuples are immutable, means that once you created a tuple you cannot modify it unlike list
t = (1, 2, 3)
# t[0] = 11  # can't do like this statement(raise error)

# 2. Tuples use parentheses() but Lists use square brackets[]
tuple = ("Apple", "Banana", "Kiwi", "Mango")
list = ["Red", "Blue", "Green", "Yellow"]

# 3. Tuples are generally smaller and faster then list because they are immutable due to which there will be less memory head
import sys
print(f"Size of list \"[1, 2, 3]\" in bytes: {sys.getsizeof([1, 2, 3])}")  # More bytes
print()
print(f"Size of tuple \"(1, 2, 3)\" in bytes: {sys.getsizeof((1, 2, 3))}")  # less bytes
print()


# Immutability
t = (1, 2, 3)  
# t[0] = 11  # Raises TypeError
# t.append(4)  # Raises AttributeError
# t.remove(1)  # Raises AttributeError
# del t[1]  # Raises TypeError
# but you can use the "del" keyword on the entire tuple
del t
# print(t)   # Raises NameError


# Immutability appplies to the tuple container, not to the object stored inside the tuple
t = (1, [4, 9])
print(f"Before modifying: {t}\n")
t[1].append(11)
print(f"After modifying: {t}\n")

# Immutable tuples can be used as key in dictionaries or stored in sets

original_tuple = (1, 2, 3)
new_tuple = original_tuple + (4, 5)
print(new_tuple)
print()


# you can also do 
original_tuple = (1, 2, 3)
original_tuple = original_tuple + (4, 5)
print(original_tuple, "\n")


# Accessing tuple elements
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(f"fruits[0]: {fruits[0]}")
print(f"fruits[-2]: {fruits[-2]}")
# slicing -> [start:end:step]
print(f"fruits[1:4]: {fruits[1:4]}")
print(f"Reverse tuple of fruits tuple: {fruits[::-1]}")
print()

# You can also create a nested tuple just like nested list
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(f"nested_tuple[0]: {nested_tuple[0]}")
print(f"nested_tuple[0][1]: {nested_tuple[0][1]}\n")

# Hetrogeneous data 
hetro_tuple = (42, "hello", [1, 2, 3], {'key': 'value'})
print(f"hetro_tuple[3]: {hetro_tuple[3]}")
print(f"hetro_tuple[3]['key]: {hetro_tuple[3]['key']}")
