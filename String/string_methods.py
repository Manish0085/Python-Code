# String Methods

txt = "Python Programming"
print(txt.upper())
print(txt.lower())

txt = "hello python programming"
print(txt.title())

print(txt.capitalize())
txt = "      hello python programming  "
print(txt.strip())
print(txt.rstrip())
print(txt.lstrip())

# string.find(substring, start, end)
txt = "Python is amazing, Python is fun"
print(f"amazing starts from index: {txt.find("amazing")}")
print(f"fun starts from index: {txt.find("fun")}")
idx = txt.find(",")
print(f"\"is\" starts from index: {txt.find("is", 19)}")

# string.find(substring, start, end)
print(f"Python occures in the \"{txt}\": {txt.count("Python")}")

# string.index(substring, start, end)
# The .index() method is similar to .find() but raises a ValueError if substring is not found
print(f"Java starts from index: {txt.find("Java")}")
# print(f"Java starts from index: {txt.index("Java")}")  # raise the error

# string.replace(old, new, count)
txt = "Hello World"
new_txt = txt.replace("World", "Python")
print(new_txt)
print(txt.replace("world", "Python")) # won't work because world doesn't exist
fruit = "banana banana banana"
print(fruit.replace("banana", "apple", 2))


# string.isalpha()
text1 = "Python"
text2 = "Python3"
print(f"\"{text1}\" contains only  alphabetic characters: {text1.isalpha()}") # True
print(f"\"{text2}\" contains only alphabetic characters: {text2.isalpha()}") # False

# string.isdigit()
text1 = "Python"
text2 = "74589"
print(f"\"{text1}\" contains only numeric characters: {text1.isdigit()}") # False
print(f"\"{text2}\" contains only numeric characters: {text2.isdigit()}") # True


# string.isalnum()
text1 = "Python@"
text2 = "Python3"
print(f"\"{text1}\" contains only alphanumeric characters: {text1.isalnum()}") # False
print(f"\"{text2}\" contains only alphanumeric characters: {text2.isalnum()}") # True

# string.isspace()
text1 = "    "
text2 = "    \n   \t"
text3 = "     \n bg'"
print(f"\"{text1}\" contains only space: {text1.isspace()}")
print(f"\"{text2}\" contains only space: {text2.isspace()}")
print(f"\"{text3}\" contains only space: {text3.isspace()}")

# string.startswith(substring, starts, end), string.endswith(substring, starts, end)
text1 = "Python is amazing."
print(f"String \"{text1}\" starts with \"Python\": {text1.startswith("Python")}")
print(f"String \"{text1}\" starts with \"Java\": {text1.startswith("Java")}")
print(f"String \"{text1}\" ends with \"Python\": {text1.endswith("Python")}")
print(f"String \"{text1}\" ends with \"amazing\": {text1.endswith("amazing.")}")


# string.split()
text = "apple,banana,orange,grape"
print(text.split(","))
text = "Python is fun to learn"
print(text.split())  # by default the split method contains the space " ".

li = ['apple', 'banana', 'orange', 'grape']
join_string = ", ".join(li)
print(join_string)

# string.format()
name = "Manish"
age = 21
msg = "Hello, my name is {} and I am {} years of old".format(name, age)
msg = "Hello, my name is {0} and I am {1} years of old".format(name, age) # positional placeholder
msg = "Hello, my name is {1} and I am {0} years of old".format(name, age)
print(msg)
msg = "Hello my name is {p1} and I am {p2} years of old".format(p1=name, p2=age) # named placeholder
print(msg)


# Old-style formatting with % operator
# string with format specifier % values

name = "Alice"
greeting = "Hello, %s!" % name
print(greeting)

'''
Common format specifier:
------------------------
%s --> String(or any object with a string representation)
%d --> Integer
%f --> Float
%x --> Hexadecimal
%o --> Octal
%.2f --> Float with precision (2 decimal places in this example)
'''
age = 20
msg = "Hello, I am %s and I am %d years old." % (name, age)
print(msg)

pi = 3.14159265359
print("Pi: %f" % pi)
print("Pi rounded to 2 decimal places: %.2f" % pi)


# String Immutability:
'''
Python strings are immmutable which means once you created a string in python then you cannot change
that string, all the methods of string craete a new string object instead of change the existing string 
'''

s = "Hello"
print(f"{s} is stored at: {id(s)}")

print(s[0])
# s[0] = "M"  # won't work
s = "M" + s[1:]
print(s)
print(id(s))

# Raw Strings 
# Raw Strings are those strings which treates the '\' as string instead of escape character.
# to make a string as raw string use 'r' character before the string like: r"string"

raw_string = r"Hello" # raw string
print(raw_string)
raw_string = r"Hel\lo"
print(raw_string)

# Print "C:\User\Vipul\Document"
print("Printing directory using string: \"C:\\User\\Vipul\\Document\"")
print(r"Printing directory using raw string: C:\User\Vipul\Document")

