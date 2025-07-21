# if - else

score = 22   # You can replace it with input func to takre the input from user
if (score >= 33):
    print("Passed!")
else:
    print("Failed!")
    print("Work hard!")

age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote!!")
else:
    print("You cannot vote yet!!")   


password = input("Enter your password: ")
if len(password) >= 8 and len(password) < 30:
    print("Valid Password!")
else:
    print("Invalid Password!!!")
    print("Password length must be equal or grater than 8 and less than 30")  

# Another example from using above input

if age >= 18:
    if len(password) >= 8 and len(password) < 30:
        print("Valid Password!")
    else:
        print("Invalid Password!!!")
        print("Password length must be equal or grater than 8 and less than 30")  
else:
    print("Chote hai aap!")
    

