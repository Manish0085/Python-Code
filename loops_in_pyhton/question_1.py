# form 1 to 20 print odd if the number is odd otherwise even  including both

for i in range(1, 21):
    result = "Even" if i % 2 == 0 else "odd"
    print(f"{i}: {result}")

# input a number from user and check that it is prime or not
num = int(input("Enter a number "))
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not prime number")
        break
if i == num-1:
    print(f"{num} is a prime number")    



# for and while both loop can have an optional else
# the else block executes after the loop finishes normally   

'''
for item in sequence:
    # Loop body
    if some_condition:
        break
else:
    # runs only if the loop was not broken 



while item in sequence:
    # Loop body
    if some_condition:
        break
else:
    # runs only if the loop was not broken               
'''

nums = [1, 2, 5, 7, 9]

for num in nums:
    if(num % 2 == 0):
        print(f"Even number found: {num}")
        break
else:
    print("Even number not found")    