# Creating a copy of list

a = [1, 2, 3]
b = a
b.append(4)
print(a)
'''
In this above code, I created a list 'a' and then assign a list a into b
when we do "a = [1, 2, 3]" it means this list [1, 2, 3] is created in memory in somewhere
and 'a' is pointing this list in memory and as we done "b = a" it means b is also pointing
to the same list in the memory. And if we modify the the list using 'b'
will also affect the list 'a'.

'''

# 1. you can create a copy of the list uisng list() constructor
b = list(a) # allows a shallow copy
print(b) # [1, 2, 3, 4] but saperate copy
b.append(5)  
print(a)  # [1, 2, 3, 4]
print(b)  #  [1, 2, 3, 4, 5]


# 1. you can create a copy of the list uisng list slicing
fruits_1 = ["apple", "banana", "kiwi", "Litchi"]
fruits_2 = fruits_1[:] # allows a shallow copy of flate list
print(fruits_2) # ["apple", "banana", "kiwi", "Litchi"] but saperate copy
fruits_2.append(5)  
print(fruits_1)  # ["apple", "banana", "kiwi", "Litchi"]
print(fruits_2)  #  ["apple", "banana", "kiwi", "Litchi", 5]


a = [[1, 2], [3, 4]]
print(a[0])  # [1, 2]
print(f"[a[0][1]]: {a[0][1]}") # 2
print(a[1])  # [3, 4]

b = a[:]  # creates a shallow copy → new outer list, but inner lists are still shared.
b[0][0] = 99  # modifies the same inner list that a[0] points to.
print(f"b: {b}") # [[99, 2], [3, 4]]
print(f"a: {a}") # [[99, 2], [3, 4]] 
print(f"id(a[0]): {id(a[0])}, id(b[0]): {id(b[0])}") # same

# That's why both a and b reflect the change.


