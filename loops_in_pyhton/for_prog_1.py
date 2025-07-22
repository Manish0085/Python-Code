# for loop
# ---------

'''
Syntax
-------

    for variable in sequence:
        # code block (loop body)

'''

fruits = ["apple", "banana", "cherry", "kiwi"]   # list of fruits
for fruit in fruits:
    print(fruit)

name = "Popatlal"
print(f"Printing character of word \"{name}\" using for loop: ")    
for ch in name:
    print(ch)

# range() function in python:
# it generates a sequence of numbers
# range(stop)                         Starts form 0 to stop-1
# range(start, stop)                  Starts form start to stop-1 
# range(start, stop, step)            Starts from start to stop-1 with increamented of step
# range() doesn't create a list in memory (unless explicitly converted)

# printing natural number in reverse order from 10 to 1
for i in range(10, 0, -1):
    print(i)

print(range(10))  # return a object of range function won't return list object unless explicitly converted
print(list(range(10)))    


fruits = ["apple", "banana", "kiwi", "papaya"]
for i in range(len(fruits)):
    print(fruits[i])
print(f"printing the loop variable i after ending the loop {i}") # printing the loop variable i after ending the loop

print("Printing the list of fruits in reverse order")
fruits = ["apple", "banana", "kiwi", "papaya"]
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i])

# In python you can access the loop variable even after the ending of the loop 

print(list(enumerate(fruits)))

# enumerate() function in python returns the list of pair of (index, element of list)
# e.g. [(0, 'apple'), (1, 'banana'), (2, 'kiwi'), (3, 'papaya')]

for idx, fruit in enumerate(fruits):
    print(fruits[idx] )
