# String is a sequence of characters enclosed within quotes.

name = "Akshit"

# Letters, Numbers, Special symbols, WhiteSpace characters, Unicode characters
print("\u0061") # unicode
print("\U0001F600") 

# u is followed by 4 digit unicode and U is followed by 8 digit unicode

language = "Python"
# How "Python" is stored in computer

# P        y       t       h       o       n
# [0]     [1]     [2]     [3]     [4]     [5]  <-- Positions/indices
print(language)
print(language[3])

print(1 + 2 * 3)
# ouput: 7
print("1 + 2 * 3")    
print('1 + 2 * 3')
# output: 1 + 2 * 3 becaue "1 + 2 * 3" is string not numbers

print(1 == 1) # True
print(1 == 2) # False

name1 = "Python"
name2 = 'Python'
print(name1 == name2) # True 

message = "Don't worry about errors"
message = 'Don\'t worry about errors'
print(message)

# '\' in python this is escape character which means the character is ignored from just one position befor it is put
dialogue = 'She said, "Python is amazing!"'
dialogue = "She said, \"Python is amazing!\""
print(dialogue)