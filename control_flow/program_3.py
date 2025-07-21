has_fever = True
has_cough = True
has_rash = False

'''
    if has_fever:
        print("Take fever medication")
    elif has_cough:
        print("Take cough syrup") 
    elif has_rash:
        print("Apply anti-itch cream") 



# all three conditions, has_fever, has_cough, and has_rash are three independent conditions 
# Just by yourself and comment this code and analyze running by youself that the output given by this
# id correct or wrong.             
'''    


if has_fever:
    print("Take fever medication")
if has_cough:
    print("Take cough syrup") 
if has_rash:
    print("Apply anti-itch cream") 




age = 25
income = 50000
if age >= 18:
    if income <= 30000:
        print("Low Income tax")
    elif income <=70000:
        print("Medium Income tax") 
    else:
        print("High Income tax")
else:
    print("No Tax because you are minor")     

'''
Test yourself by finding the error in the following code:

x = int(input("Enter the value of x: "))
if x = 5:
    print("x is 5")
'''     


# a --> 5, 7, 9 ---> lucky
# else --> unlucky
a = 9
if a == 5 or a == 7 or a == 9:
    print("Lucky")
else:
    print("Unlucky")    

# we can do the above thing using the list as follows:
if a in [5, 7, 9]:
    print("Lucky")
else:
    print("Uncluck")    