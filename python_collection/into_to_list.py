# A built-in data structuure that stores an ordered, mutable collection of item 
# Lists can hold items of any type, including other lists


# Ordered: Items have a defined order and can be accessed by their index
# Mutable: You can change, add or remove items after the list has been created.
# Heterogeneous: A single list can contain element of different data types
# Iterable: Lists can be looped over using for loops  or comphrehensior 

# creating List
# -------------
# list_name = [list item separated by comma]

my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]

# Nested List(List inside list)
nested_list = [[1, 2], [3, 4]]

# List of Strings
colors = ['red', 'green', 'blue']

# List of boolean
flags = [True, False, True]

# List of mixed Types
info = ['alice', 30, 5.5, False]


# List inside list
matrix = [[1, 2], [3, 4], [4, 5]]
'''
1 2
3 4
4 5
'''

# To create  a list use always square brackets, don't use parenthesis'()'
# if you use parenthesis'()', that will be tupple not list 

# You can also create a list using list constructor() and this list constructor either expects one arg or no arg
# you can give only itreator as an argumment in the list constructor. 
li = list() # as good as []

li = list("Hello")
print(li)
print(list(range(10)))

original_list = [1, 85, 64, 5]
copied_list = list(original_list)
# list function is also used to create a copy of the list

# think by yourself 
# print(list(123))
# this line will execute or give error
