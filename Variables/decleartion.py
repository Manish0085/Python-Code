# How to declera variables in python
a = 1
b = 2
c = 3.0
print(a, b, c)
# Output: 1 2 3.0
print(a, b, c, sep=", ")
# Output: 1, 2, 3.0

# We cannot declear the variables in python in a sigle as below 
#a = 1, b = 2, c = 3.0
# print(a, b, c)

# if you want to declear the multiple varible in single line use the following syntax
x, y, z = 4, 5.0, 8.9
print(x, y, z)  
# Output: 4 5.0 8.9
print(x, y, z, sep=", ")
# Output: 4, 5.0, 8.9

# we haven't give any space in the print function even then the out for printing a, b, c 
# is space separated it is because the print function internaly execute a varible called "sep" ehich has the default 
# value is sep = " " and the print function execute this varaible after printing each variable specified to saperate sumtiple 
# variables. We can also change the value of this sep variable according to the requirement.

print(a, b, c, sep=", ")
# Output: 1, 2, 3.0