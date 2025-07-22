num = int(input("Enter the number upto which you want to print the natural number "))

x = 1
while x <= num:
    print(x)
    x += 1

print(f"Printing natural number upto {num} using for loop")
for i in range(1, num+1):
    print(i)    