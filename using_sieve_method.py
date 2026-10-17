#Sieve Eratosthenes Method...

def sieve(num) :
    
    
    prime  = [True]*(num+1)
    p = 2
    
    while p*p <= num :
        if prime[p] :
            for i in range(p*p,num+1,p) : 
                prime[i] = False 
        p += 1   
    res = []
    
    
    for p in range(2,num+1) :
        if prime[p] :
             res.append(p)
    
    return res


number = int(input("Enter numbers for primes : "))


# print(sieve(number)) 

res = sieve(number)



for ele in res : 
    print(ele, end=' ') 



# numbers of prime in that range . 
print(f"Number of prime {len(res)}")


    