# factorial numbers 

import math
number = int(input("Enter a number :  "))

# interative method ...


'''
fact=1
for i in range(1,number+1) :
    fact *=i 
'''





# build in library...
# print(math.factorial(number))





# using recursion...

def fact(n) :
    if n<0 :
        return "Factorial is not defined for negative numbers "
    
    return 1 if n<=1 else n*fact(n-1)


print(fact(number))
