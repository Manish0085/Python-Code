# How to store line string
# Either using '\n' which is called new line character or bu using ''' ''' tripple quotes 
poem = "Chasing dreams beneath the sky, \nWith hope in heart and stars up high, \nEach step forward, we learn to fly. "

poem = '''Chasing dreams beneath the sky,
With hope in heart and stars up high,
Each step forward, we learn to fly. '''

print(poem)

poem = """Chasing dreams beneath the sky,
With hope in heart and stars up high,
Each step forward, we learn to fly. """
print(poem)

# Print "C:\User\Vipul\Document"
path = "C:\\User\\Vipul\\Document"
print(path)

print("HEL\"P")
print("HEL\nP") # add a new line character '\n'
print("HEL\tP") # add a tab '\t'
print("hel\\lo") # ignore one '\' and will print 'hell\o'
# print("HELP\U") # use unicode after '\U'