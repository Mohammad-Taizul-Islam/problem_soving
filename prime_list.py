# numbers = [int(x) for x in input("Enter numbers seperated by space : ").split(' ')]

numbers = [int(x) for x in input("Enter numbers seperated by space : ").split()]

for num in numbers :
    print(num ,end=' ')
    print("\n")
def sieve_up_to(n):
    s=[True] * (n+1)
    s[0]=s[1]=False
    for i in range(2,int(n**0.5)+1) :
        if s[i] : 
            for j in range(i*i,n+1,i) : 
                s[j] = False
    return s

limit = max(numbers)

is_prime = sieve_up_to(limit)

results =[is_prime[n] for n in numbers]


for n,prime in zip(numbers,results) :
    
    print(f"{n} -> {'Prime' if prime else 'Not prime'}")


'''

def isPrime(n) : 
    if n == 2 :
        return True 
    elif n == 1:
        return False
    else : 
        s = [True]*(n+1)
        s[0]=s[1]=False
        
        for i in range(2,int(n**0.5)+1) :
            if s[i] : 
                for j in range(i*i,n+1,i) :
                    s[j] = False
        
        return s[n]


def sievePrimeList (numbers) :
    res = []
    for i in numbers :
        prime = isPrime(i)
        if prime :
           return res.append(i)
        else :
            return res

print("My Prime number : ",sievePrimeList(numbers))


'''
