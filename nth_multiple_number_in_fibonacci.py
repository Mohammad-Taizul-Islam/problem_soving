#nth multiple of a numer in Fibonacci Series...

# iterative method...

'''
def nth_multiple_fibonacci(n,m) :
    a,b,count = 0,1,0
    
    while True :
        a,b=b,a+b
        
        if b%m == 0 :
            count+=1
            if count == n :
                print(b)
                break
            

'''

# Dynamic Programming ...


'''
def nth_multiple_fibonacci(n,m) :
    fib = [0,1]
    
    count = 0
    
    while True :
        fib.append(fib[-1]+fib[-2])
        
        if fib[-1] % m == 0 :
            count += 1
            if count == n :
                return fib[-1]
            

'''


#Recursive Approach with Memoization ...

def nth_multiple_fibonacci(n,m) :
    

input_number = int(input("Enter a number of Finding in Fibonacci Series L:"))

multiple_number = int(input("Enter a number of multipler : "))

print(nth_multiple_fibonacci(input_number,multiple_number))