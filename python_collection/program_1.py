day1_temp = 72
day2_temp = 75
day3_temp = 71
day4_temp = 74

average = (day1_temp + day2_temp + day3_temp + day4_temp) / 4


temps = [72, 75, 71, 74]
average = sum(temps) / len(temps)


# The purpose of the above code is just to tell you that whenever you have large number of data value and you need to store them
# then instead of storing them in the separate variable you can use the list(data structure) collection in python which provides you flexiblity to
# play with data and provides many inbuilt functions as you can see the sum() function.

# In python, we can break the data in three types:
#       --> seuences - string, list, tuple
#       --> mappings - dictionary
#       --> sets     - set, frozenset

# string - Ordered, immutable sequence of characters
#        - "Hello World"

# list - Ordered, mutuable collection that can contain misxed data types 
#      - [1, "hello", 3.14, True]

# tuple - Ordered, immutable collection similar to lists
#       - (1, "hello", 3.14, True)

# dictionary - Unordered (pre-3.7) / insertion-ordered (3.7+) key-value pair
#            - {'name': 'Alice', 'age': 25, 'city': 'New York'}

d = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(d['name'])

# set - Unordered mutable collection of unique element
#     - {1, 2, 3, 5}

# frozenset - Unordered immutable collection of unique element
#           - Immutable version of set
#            - {1, 2, 3, 5}


