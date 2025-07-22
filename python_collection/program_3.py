fruits = ['apple', 'banana', 'cherry']
print(f"List before modiying: {fruits}")
fruits[1] = 'blue berry'
# we can also replace the multiple values using slice
fruits[1:3] = ["banana", "date"]
print(f"List after modiying: {fruits}")

# methods for list:
# 1. append()
fruits.append('mango')  # append new element at the lat of the list
print(fruits)  # ['apple', 'blue berry', 'cherry', 'mango']4


# 2. insert()
fruits.insert(2, 'orange')  # insert the item at the specified index
print(fruits)  # ['apple', 'blue berry', 'orange', 'cherry', 'mango'] 


# 3. extend()
fruits_2 = ["grapes", "kiwi"]
fruits.extend(fruits_2)  # append would add the entire list as a single element
print(fruits)  # ['apple', 'blue berry', 'orange', 'cherry', 'mango', 'grapes', 'kiwi']


# 4. remove()
fruits.remove("orange")  # remove takes the object to be removed
print(fruits)  # ['apple', 'blue berry', 'cherry', 'mango', 'grapes', 'kiwi']


# 5. pop()
fruits.pop(4)  # remove the element from the specified index
print(fruits)  # ['apple', 'blue berry', 'cherry', 'mango', 'kiwi']
# if you don't specify the index then last element form the list will be removed
# you can also specify the negative index
# remove method returns nothing but the pop method returns the popped element
# needs a valid index otherwise error will be thrown

# del is a keyword not a method which helps you to delete uisng slicing or index unlike it returns nothing
del fruits[1:3] # ['apple', 'mango', 'kiwi']
print(fruits)

# 6. clear(): remove all the items from the list and the list becomes empty
fruits.clear()
print(fruits) # []