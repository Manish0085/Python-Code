a = [1, 2, 3]
b = [4, 5]
result = a + b
print(result) # similar to extend
# when we use extend() method, original list is chnaged but when we use '+' operator then a new list is created 


# result = a + b + 6  # wrong
# result = a + b + [6]  # wrong

print(a * 3)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# list elements will be repeating 

# create a list of length 5 in which all the elements are 0
list = [0] * 5
print(list)


fruits = ["apple", "banana", "cherry"]
print(fruits.__contains__("apple"))  # True
print(fruits.__contains__("kiwi")) # False
# or you can use 'in' key word
print("banana" in fruits)
print("guavava" in fruits)
print("guavava" not in fruits)  # uses linear search

nested = [[0] * 3] * 3 # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(nested)
nested[0][0] = 1
print(nested)

# nested = [[0] * 3] * 3 creates  shalllow copy not deepcopy that's why all three inner list are updated just doing 
# nested[0][0] = 1

print(f"\"he\" in \"hello\": {"he" in "hello"}")

# try to analyze the answer without executing the code
print(f"len([1, 2, 3, [4, 5]]): {len([1, 2, 3, [4, 5]])}")

numbers = [10, 5, 8, 3]
print(f"min({numbers}): {min(numbers)}")
print(f"max({numbers}): {max(numbers)}")
print(f"sum({numbers}): {sum(numbers)}")

names = ["Alice", "Bob", "Charlie"]
print(f"min({names}): {min(names)}")
print(f"max({names}): {max(names)}") # compares alphabetically not on the basis of length






