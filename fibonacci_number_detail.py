#simple naive approach using recursion ...

'''
def nth_fibonacci_number (n) :
    if n<=1 :
        return n
    else :
        return nth_fibonacci_number(n-1) + nth_fibonacci_number(n-2)
'''
# Bottom_to_up method...

'''

def nth_fibonacci(n) :
    if n <= 1 :
        return n
    dp =[0]*(n+1)
    
    dp[0],dp[1]=0,1
    
    
    for i in range(2,n+1) :
        dp[i] = dp[i-1]+dp[i-2]
    
    return dp[n]
'''

def nth_fibonacci(n,m) :
    fib = [0,1]
    count = 0
    while True :
        fib.append(fib[-1]+fib[-2])
        if fib[-1] % m == 0 :
            count+=1
            if count == n :
                return fib[-1]


input_number = int(input("Enter a number for N'th Fibonacci Number : "))
print(f"Nth Fibonacci Number : {nth_fibonacci(input_number)}")
