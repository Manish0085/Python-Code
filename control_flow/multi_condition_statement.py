'''
if condition1:
    # Code Executed whien condition1 is True
elif condition2:
    # Code executed when condition1 is False And condition2 is True
elif condition3:
    # Code is executed when condition1 and condition2 are False And condition3 is True    
else:
    # Code is executed when all conditions are False

'''

score = int(input("Enter youre score: "))
if score > 90:
    grade = "A"
elif score > 80:
    grade = "B"
elif score > 70:
    grade = "C"
elif score > 65:
    grade = "D"
elif score >=33:
    grade = "E"
else :
    grade = "F" 

print(f"Your grade is {grade}")    



tempreature = int(input("Enter temperature: "))
if tempreature < 32:
    print("It is freezing. Wear heavy coat.")
elif tempreature < 50:
    print("It's cold. Wear a jacket.")    
elif tempreature < 70:
    print("It's cool. Bring a light sweater.")
elif tempreature < 85:
    print("It's warm. T-shirt weather!")
else:
    print("It's hot. Stay hydrate.")        




#