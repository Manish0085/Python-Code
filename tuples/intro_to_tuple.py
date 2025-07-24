# A tuple is an ordered, immuatable collection of items.
# Once we created a tuple, we cannot change the tuple data that's why it is less flexible and more memory efficient

my_tuple = (1, 2, 3) # Also you can avoid the parenthesis and put the values in the tuple separated comma
another_tuple = 1, 2, 3

a = 1, 2  # tuple
print(f"type(a = 1, 2): {type(a)}")
print()
a = 1 # not a tuple
print(f"type(a = 1): {type(a)}")
print()
a = (1) # not a tuple
print(f"type(a = (1)): {type(a)}")
print()
a = (1, ) # tuple(Comma indecates that this is a tuple)
print(f"type(a = (1, )): {type(a)}")
print()


# tuple constructor
tuple_from_string = tuple("abc")
print(f"Tuple form string: {tuple_from_string}")  # ('a', 'b', 'c')
print()


tuple_from_list = tuple([1, 2, 3])
print(f"Tuple form list: {tuple_from_list}")
print()


# Thing that below statement will create a tuple or not
# t = tuple(5) # TypeError: 'int' object is not iterable
# t is not a tuple and also throw an error because the tuple constructor also requires an iterable
# but you gave an integer object hence t is not a tuple
# if you want to create a tuple which has single value using tuple constructor then use the following statement:
# t = tuple([5])
t = tuple([5]) 

# creatin empty tuple
empty = ()  # way to create empty tuple
empty = tuple() # you can also create a empty tuple using tuple constructor


 





