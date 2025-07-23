# find min in list
numbers = [4, 5, 6, 67, 7, 1]
min = numbers[0]
for i in range(len(numbers)):
    if min > numbers[i]:
        min = numbers[i]

print(f"Minimum in {numbers}: {min}")    # 1    
print()

# find max
max = numbers[0]
for i in range(len(numbers)):
    if max < numbers[i]:
        max = numbers[i]

print(f"Maximum in {numbers}: {max}")  # 67