#mathemetical approach...

number = int(input("Enter number : "))

# iterative method...
'''
t = number

p =len(str(number))

armnumber = 0
while t > 0 :
    d = t%10
    armnumber += d**p
    t//=10
    
if armnumber == number :
    print("Armstrong number !")
else :
    print("Not an armstring number ")
'''


# using string...

'''
p = len(str(number))
s = sum(int(d) **p for d in str(number))
if s == number :
    print("Armstrong number")
else :
    print("Not an armstrong number")
'''


# using map and lambda...
p=len(str(number))
s = sum(map(lambda  d : (int(d)**(number))))

if s == number :
    print("Armstrong number")
else :
    print("Not an armstrong number")
