# if you to avoid shared behaviour of list and make a complete separate copy 
# then use the copy module

import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
print(b)
b[0][0] = 99
print(f"a: {a}")
print(f"b: {b}")
print(f"id(a[0]): {id(a[0])}, id(b[0]): {id(b[0])}")