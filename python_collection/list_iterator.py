fruits = ["apple", "banana", "kiwi", "mango", "orange", "papaya", "Apple"]
for fruit in fruits:
    print(fruit, end=" ")

print()
# using index
for i in range(len(fruits)):
    print(fruits[i], end=" ")    

print("\n")


# count occurrence of a item in list uisng loop
count = 0
for i in range(len(fruits)) :
    if fruits[i] == 'apple':
        count += 1
print(f"\"apple\" count in {fruits}: {count}") 
print()



# find the index of a item in list uisng loop
idx = -1
for i in range(len(fruits)):
    if fruits[i] == 'orange':
        idx = i
        break

print(f"first occurrence of \"orange\" in {fruits} at index: {idx}")
print()

# Reverse a list using loop
reversed_list = []
for i in range(len(fruits)-1, -1, -1):  # can also be used slicing for i in fruits[::-1]:
    reversed_list.append(fruits[i])

print(f"Reverse of {fruits}: {reversed_list}")    
   