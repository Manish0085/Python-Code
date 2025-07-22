'''
while loop syntax:
-------------------

while conditon:
    # code block to be executed
    # updation

    
1. Pyhton checks the condition first.

2. If the condition specified is true, it executes the intented block.

3. After the block execution, updation takes place if mention inside while loop for checking the condition ahead.

4.  Again the condition is checked by python interpreter
        --> If the contidiion is still True, it repeates the task.
        --> If it becomes False, the loop stops

# while loop is also known as entry control loop. 
# the loop condition must become False at a point, otherwise the loop will go on for infinite time
# hence always write updation statement indside the while loop.
# If you want to exit from the loop at a perticular condition without envoking the loop completely then 
# you can use the break statament like the following:
#  
'''



x = 5
while x <= 10:
    print("While loop in python")
    x += 1

while x <= 10:
    print("Use of break statement in python")
    if x ==3:
        break
    x += 1

# Here I have Question for you:
#   the second while loop won't execute even the flow won't go inside this while loop block
#   thik why it happened by yourself.   


'''

while True:
    print("Ok)

this loop will go on for infinite time hence always try to avoid this boolean as conditions directly.       

'''