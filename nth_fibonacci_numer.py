# Nth Fibonacci number
# Naive approach...(using recursion) :

'''
def nth_fibonacci(n) :
    if n<= 1 :
        return n
    
    return nth_fibonacci(n-1) + nth_fibonacci(n-2)

'''


# Memoization Approach...(using recursion)

'''
def nth_fibonacci_util(n,dp) :
    if n<= 1 :
        return n
    if dp[n] != -1 :
        return dp[n]
    dp[n] = nth_fibonacci_util(n-1,dp)+nth_fibonacci_util(n-2,dp)
    
    return dp[n]

def nth_fibonacci(n) :
    dp = [-1]*(n+1)
    
    return nth_fibonacci_util(n,dp)
'''

# Bottom up Approach...(recursion)
'''
def nth_fibonacci(n):
    if n<=1:
        return n
    dp = [0]*(n+1)
    dp[0],dp[1] = 0,1
    
    for i in range(2,n+1) :
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]



'''

# Bottom Up Space Optimazation 
'''
def nth_fibonacci(n):
    if n <= 1:
        curr=0
        prev1 = 1
        prev2 = 0
        
        for i in range(2,n+1) :
            



'''

# using Matrix exponentiation...





# input number...

input_number = int(input("Enter a numer for it's Nth Fibonacci : "))

print(f"Nth Fibonacci number : {nth_fibonacci(input_number)}")
