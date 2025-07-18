# To gat the license, you must have the Aadhaar card *AND* your gae must be equal and graeter than 18 --> DL

has_aadhaar = True
age = 17
print(f"has_aadhaar({has_aadhaar}) and age({age}) >= 18: {has_aadhaar and age >= 18}") # False


# to get entered in the club, you must have DL *OR* Aadhaar card

has_DL = True
has_aadhaar = False
print(f"has_aadhaar({has_aadhaar}) or has_DL({has_DL}): {has_aadhaar or has_DL}")


# to play cricket, *NOT* injury

has_injury = True
print(f"not has_injury({has_injury}): {not has_injury}")


x = 5
y = 15
print(f"{x} > 0 and {y} > 0: {x > 0 and y > 0}" )
print(f"{x} > 7 and {y} > 0: {x > 0 and y > 0}" )

# 'or' operator need alteast one true value to give result 'True' and as soon as one value becomes true interpreter won't go ahead to check
# because as soon as one value becomes true the result becomes true
age = 25
income = 30000
print(f"age({age}) > 18 or income({income})> 50000: {age > 18 or income > 50000}")
print(f"age({age}) < 18 or income({income})> 50000: {age < 18 or income > 50000}")
print(f"age({age}) < 18 or not(income({income})> 50000): {age < 18 or not(income > 50000)}") 
# age < 18 or not(income > 50000) --> 
#       age < 18 --> False
#       (income > 50000) --> False
#       not((income > 50000)) --> True
# Also called as Short-Circuit Evaluation


# Boolean Operator Precedence
# not > and > or
result = True or False and not True
#        True or False and not True
#        True or False and False  (Because not True becomes False)
#        True or False            (Because (False and False) becomes False) 
#        True                     (Because (True or False) becomes True) 
print(f"(True or False and not True): {result}")

result = (True or False) and (not True)
#       (True or False) and (not True)
#        True and False           (Because not True becomes False and (True or False) beacomes True)
#        False                    (Because (True and False) becomes False) 
print(f"((True or False) and (not True)): {result}")


age = 25
salary = 30000
credit_score = 700
is_eligible = (age >= 18 and age <= 65) and (income > 25000 or credit_score > 650)
#             (age >= 18 and age <= 65) and (income > 25000 or credit_score > 650)
#             (25 >= 18 and 25 <= 65) and (30000 > 25000 or 700 > 650)
#             (True and True) and (True or True)
#              True and True  --> True
print(f"(age({age}) >= 18 and age({age}) <= 65) and (income({income}) > 25000 or credit_score({credit_score}) > 650): {is_eligible}")



working_age = age >= 18 and age <= 65
print(f"Working age according to (age({age}) >= 18 and age({age}) <= 65): {working_age}")

# In Python, We can also do like
working_age = 18 <= age <= 65
print(f"Working age according to (18 <= age({age}) <= 65) <= 65): {working_age}")

print(f"(not age({age}) >= 18) or (not income({income}) > 25000): {(not age >= 18) or (not income > 25000)}")


# Comparision Operators: '!=', '==', '<=', '>=', '<', '>'