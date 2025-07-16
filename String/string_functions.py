# len() function
a = "python"
print(f"lrngth of {a} is {len(a)}")

print(len(""))
print(len("Hello\nWorld")) # output: 11
print(len("❤️")) # output: 2
print(len("😀")) # output: 1
print("\u2764")
print("\uFE0F")
print("\u2764\uFE0F")

msg = "Help!"
# print(len(msg) == 5)
bool = len(msg) == 5;
print(bool)

# ord() print asic value 
print(ord("A")) # 65
print(ord("a")) # 97

# chr() gives the character corresponding to the deciaml
print(chr(97))
print(chr(65))