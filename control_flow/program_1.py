age  = int(input("Enter your age "))
if age >= 18:
    print("Inside if block")
    print("You ra adult")

print("outside if block")    


temp = int(input("Enter the temperature "))
is_raining = bool(input("Leave empty if not raining else type anything "))
if temp < 10 and is_raining:
    print("Wear the jacket")


# Python evalutes this name variable as truthy and falsy and in this case pyhton interpreyter will treate the name as false because it is empty string
# and the if block won't execute
name = ""  
if name: 
    print("If block won't execute if name is empty")  


# this is nezted condition
temp = 5
is_snowing = False
if temp < 10:
    print("It is freezing!")
    print("Wear a heavy coat.") 
    if is_snowing:
        print("And don't forget your boots!")

print("Have a nice day!")
# For above example consider a scenario in which temp is 15 and analyze the output by yourself first without directly running 

money = 300
is_free_popcorn_available = True
if money >= 400:
    print("Move dehkne gye")
    if is_free_popcorn_available:
        print("Popcorn khaye!")


# If you want to ignor some conf=dition or don't want to execute any after meeting some specific condition
# you have to write the python keyword 'pass' in that block which tells to the python interpreter that ignore this perticular block or stuff   

score = 89
if score > 90:
    print("Excellent!")
    print("Keep up the good work!")
if score < 60:
    pass       # this perticlar block is ignored by python interpreter
print("You need to study more")         