
def isPrime(n) : 
    if n <= 1 :
     print(False)
    else :
      prime = True
    
      for i in range(2,int(n**0.5)+1) :
        if n % i == 0 :
            prime = False
            break
    return prime


def sieve(nums) :
    res = []
    
    for num in nums :
        res.append(isPrime(num)) 
    
    
    return res
    
numbers = [int(x) for x in input("Enter numbers seperated by space : ").split()]
print("My List : \n",sieve(numbers))  