#Baive approach (using iteration)...

def power(b,e):
    pow=1
    
    for i in range(abs(e)) :
        pow = pow*b
    
    if e < 0 :
        return 1/pow
    
    return pow
        
base =float(input("Enter a number for base : "))
expo =int(input("Enter a power for operation : "))

print(power(base,expo))