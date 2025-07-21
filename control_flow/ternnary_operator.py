'''

Ternary Operator:
------------------
The ternary operator in Python lets you write an if-else decision in just one line.
You use it when you want to choose a value depending on a condition.
Other languages like Java uses '? and :' in tarnary operator.  (Aviod this line if Python is your first Programming language)



if condition:
    result = value1
else:
    result = value2

result = value1 if condition1 else condition2   

General Syntax:
---------------
                variable = value_if_true if condition else value_if_false

'''
'''
age = 10
if age >= 18:
    print("Adult")
else :
    print("Minor")    
'''

age = 10
status = "Adult" if age >= 18 else "Minor"
print(status)



number = 17
divisor = 0

result = number / divisor if divisor != 0 else "Cannot be divided because divisor is zero"
print(result)


operation = input("sub or add? ")
a, b = 7, 5
result = a + b if operation == "add" else a-b if operation == "sub" else "Unknown Operation"
print(result)