# can be positive, negative and zero

a = 10
b = -22
c = 0
print(a, b, c)
print(type(a))

# Python integer have unlimited precision
a = 4125987555454123669621112226366549879252
print(a)
print(type(a))

# to increase the readability of the number python allows you to use the "_" underscore in the number 
# python interpreter will ignore these underscores.
salary = 10_00_000
print(salary)

binary_number = 0b10001
print(binary_number) # print the decimal of the binary if you want to print the binary representation then use the bin() method
print(type(binary_number))
binary_number = 101010  # not binary number if you want to store the binary number in python add preffix '0b' in thet number
binary = bin(binary_number)
print(binary)
print(bin(10))

# to store the hexa decimal in binary add the preffix '0x' in the number in python
hexa_num = 0x2A
print(hexa_num)  # print in decimal fromat