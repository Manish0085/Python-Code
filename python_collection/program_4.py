# == vs is

a = [1, 2, 3]
b = [1, 2, 3]
print(f"id(a): {id(a)}, id(b): {id(b)}")
print(f"\"a == b\": {a == b}")
print(f"\"a is b\": {a is b}")  # is checks that the memory location is same of both or not 

print()
b = a
print(f"id(a): {id(a)}, id(b): {id(b)}")
print(f"\"a == b\": {a == b}")
print(f"\"a is b\": {a is b}")
print()


 
a = [1, 2, 3]
b = a
b.append(4)
print(a) # [1, 2, 3, 4]
print()

# store the square of the following list in the new resultant list
list = [1, 2, 3, 4, 5, 6, 7]
result = []
for i in list:
    result.append(i**2)
print(result)  
print()

# list comprehension
# new_list = [expression for item in iterable]
res = [i ** 2 for i in list]
print(f"Using list comprehension: {res}")
print()

# find square of first 10 natural number
result = [i ** 2 for i in range(1, 11)]
print(f"square of first 10 natural number: {result}")

# find the square of first even number upto 10
# result = [i**2 for i in range(2, 11, 2)]
result = [i**2 for i in range(1, 11) if i % 2 == 0]
print(f"even numbers square: {result}")
print()

result = [ i ** 2 if i%2 == 0 else i for i in range(1, 11)]
print(result)
print()

drinks = ['coffee', 'tea']
deserts = ['cake', 'cookie', 'ice cream']
result = [(i, j) for i in drinks for j in deserts]
print(result)
print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flate_of_matrix = [j for i in matrix for j in i]
print(flate_of_matrix)
print()

text = "Python list comprehension is powerful ans concise"
split_text = text.split(' ')
extracted_words = [word for word in split_text if len(word) > 5]
print(extracted_words)



