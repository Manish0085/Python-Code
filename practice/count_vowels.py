
# Count the number of vowels in a given string.
str = input("Enter any string ")

count = 0
for ch in str:
    if(ch == 'a' or ch == 'A' or ch == 'e' or ch == 'i' or ch == 'E' or ch == 'I' or
       ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
        count += 1

print(f"{str} has {count} vowels") 


count = sum(1 for ch in str if ch in 'aeiouAEIOU')

print(f"{str} has {count} vowels") 










