
number1 = int(input("Enter a number :  "))
number2  = int(input("Enter a number :  "))

#print(max(number1,number2))


def maximum(a,b) :
    
    if(a>b) :
        return a
    else : 
        return b
    
    # Ternary Operator..
    # return (a if a > b else b)



print(maximum(number1,number2))