name = input("Enter your name ")
age = int(input("Enter your age "))

print(f"Hello {name}! You will be {age + 5} years old in 5 years.")

# In the above statements where I have taken the input form user the,
# while taking the age, I used the int() method to convert the input into integer
# but in the name I didn't do anything like this beacuse by default input()
# function takes the input as string.


# analyze the output:
a = 10
b = "20"
print(f"a + int(b): {a + int(b)}")


# Create a program that checks whether the given number is even or odd.
num = int(input("Enter a number "))
result = "Even" if num % 2 == 0 else "Odd"
print(f"{num} is {result}")


