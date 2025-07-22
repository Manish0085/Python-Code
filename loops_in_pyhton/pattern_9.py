'''
* * * * * * * * *
* * * *   * * * * 
* * *       * * *
* *           * *
*               *
* *           * * 
* * *       * * *
* * * *   * * * *
* * * * * * * * *


'''


for i in range(1, 10):
    for j in range(1, 10):
        if j <= 6-i or j >= 4+i or j <= i or j >= 10-i :
            print("*", end=" ")
        else:
            print(" ", end=" ")    
    print() 