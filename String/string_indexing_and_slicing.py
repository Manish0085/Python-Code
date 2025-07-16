# String Indexing and Slicing

txt = "Python"
# print(f"txt[len(txt)]: {txt[len(txt)]}") will give error
print(f"txt[len(txt) - 1]: {txt[len(txt) - 1]}") # n
# txt[len(txt) - 1] = txt[5]
# len(txt) = 6
# len(txt) - 1 = 5, becaue the indexing in the programming languages starts from 0.

'''
String:     P       Y       T       H       O       N
Index:      0       1       2       3       4       5
Neg Index:  -6      -5      -4      -3      -2      -1
'''

print("txt[-1]: {txt[-1]}")
# print("txt[-1]: {txt[-7]}") will give error
# {txt[len(txt) - 1]} and {txt[-1]} will give the same result

# Slicing: Extract the substring
# syntax: string[start: end: step]
# step: no. of char to be skipped or shows the internal between characters by default its value is 1 which indecates that every char is to be added
# start: inclusive
# end: exclusive

txt = "Python Programming"

slice = txt[0:6]
print(slice)


'''
P       y       t       h       o       n               P       r       o       g       r       a       m       m       i       n       g
0       1       2       3       4       5       6       7       8       9       10      11      12      13      14      15      16      17
-18     -17     -16     -15     -14     -13     -12     -11     -10     -9      -8      -7      -6      -5      -4      -3      -2      -1   
'''

print(f"txt[7:18]: {txt[7:18]}")
print(f"txt[7:]: {txt[7:]}")
print(f"txt[:6]: {txt[:6]}")
print(f"txt[:]: {txt[:]}")

print(f"Using positive index txt[7:10]: {txt[7:10]}")
print(f"Using negative index txt[-11:-8]: {txt[-11:-8]}")


# Print Pto form Python
print(f"txt[:6:2]: {txt[:6:2]}")

# A Negative step traverses the string in reverse direction
print(f"txt[::-2]: {txt[::-2]}") # Skip one character starting from end of string

# reverse string
print(f"Reverse(txt[::-1]) of {txt}: {txt[::-1]}")