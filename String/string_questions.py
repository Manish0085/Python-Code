# String Question
# String Method Chaining

# Ques: strip, capitalize the first letter of each word, and replace "SKILLS" with "Expercise"
text = "    python programming SKILLS   "

new_text = text.strip().title().replace("Skills", "Exercise")
print(f"Updated string is: {new_text}")


# 2. Advance slicing challange
# Print every second character using slicing
# Print the string in reverse order using slicing
# Extract and print just "Programing" using negative indices
text = "Python Programming Language"
print(f"Every second character of string \"{text}\": \"{text[::2]}\"")
print(f"Reverse of string \"{text}\": \"{text[::-1]}\"")
print(f"\"Programming\" word in the string \"{text}\" is at index: {text.find("Programming")}")


# 3. String Concatination and Slicing 
# create a new string by extracting the first letter of each word and concatinate them 
text = "python is easy to learn"
ans = text[0] + text[7] + text[10] + text[15] + text[18]
print(f"the new string craeted by concatinating the first letter of the each eord of the string \"{text}\": \"{ans}\"")


# 4. String Palindrome check
word = "radar"
print(f"\"{word}\" is palindrome: {word == word[::-1]}")

# 5. find the occurrences of 'i', 's', 'p' and 'm'  
text = "mississippi"
print(f"\"i\" occures {text.count("i")}\n\"s\" occures {text.count("s")}\n\"p\" occures {text.count("p")}\n\"m\" occures {text.count("m")}")
