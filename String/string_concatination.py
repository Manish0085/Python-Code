# String Concatination

a, b = 1, 2
print(a + b) 
# output: 3

a, b = "1", "2"
print(a + b)
# output: 12

first_name = "Shubham"
last_name = "Sharma"
print(first_name + " " + last_name)


# Python mutiline comment
'''
age = 45
message = "My age is " + age
print(message) 

Python interpreter is executing the code line by line and as soon as the interpreter will come to  the cuuent code
which we make the multiline string but not assign it to any variable then pythin interpreter will craete the object of this string 
and give memory to it but it will destroy this object as soon as it see that this string is not assigned to any of the oject or variable.

'''

age = 45
message = "My age is " + str(age)
print(message)

city = "New York"
temp = 75
weather_report = "The temperature in " + city + " is " + str(temp) + " degrees"
print(weather_report)

# fString automaticaly type cast a variable of any type into string.

'''
    In fString the {} curly brackets tells to the python interpreter that 
    the word enclosed in {} is not just a word rather is a varible whose value is to be printed
'''
weather_report = f"The temperature in {city} is {temp} degrees"
print(weather_report)

a, b = 5, 10
print(f"The sum of {a} and {b} is {a + b}")


name = "Vipul"
print(f"First character of {name} is " + name[0])
print(f"First character of {name} is {name[0]}")


# Print "This is a curly brace: {" using fString
# print(f"This is a curly brace: {") // give error
print(f"This is a curly brace: {{")


a = 3
print(a * 3) # 9
b = "pyhton"
print(b * 3)

star = "* "
print((star * 5 + "\n") * 5)

a = "python"
print(a * 0) # string will be empty but a has the value python beacue in python as
             # we perfrom any operation on string a new string creates each time
print(a * -1) # string will be empty

# Print PyPythonthon
str1, str2 = "Py", "thon"
print(str1*2 + str2*2)

