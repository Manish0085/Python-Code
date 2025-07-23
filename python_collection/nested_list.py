[
    [1, 2, 3],  # 0th element
    [4, 5, 6],  # 1st element
    [7, 8, 9]   # 2nd element
]

cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]
print(f"cube[1][1][0] from {cube}: {cube[1][1][0]}")


nested = [1, [2, 3]]
# print(nested[0][1])   # error
print(nested[1][1])



matrix = [
    [1, 2, 3],  # 0th element
    [4, 5, 6],  # 1st element
    [7, 8, 9]   # 2nd element
]
matrix[0][0] = 11
print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()    

print()

z_list = [
    [1, 85, 96, 45],
    [41, 52],
    [333], 
    [41, 31]
]

for raw in z_list:
    for i in raw:
        print(i, end=" ")
    print()  
    
      