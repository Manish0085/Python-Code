# List indexing and slicing

fruits = ['apple', 'banana', 'cherry']
print(fruits[0])   # apple
print(fruits[2])   # cherry
print(fruits[-1])  # cherry


numbers = [10, 20, 30, 40, 50]
# list[start: end: step]
print(numbers[0:3])  # as good as numbetrs[:3]
print(numbers[:])
print(numbers[1::2])

# if you go out of range while playing with slicing then python won't give error 
print(numbers[0:22])

# geeting last element of the list
print(f"last number of the list is: {numbers[len(numbers) - 1]}")

# reverse the list
print(f"Reversing the list uding slicing: {numbers[::-1]}")

# Slicing always return a new list after slicing the list instead of modifying the same one

# print the last three number of list number uisng negative index
print(numbers[-3:])

