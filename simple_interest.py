#simple interest ... novice approach...

principle = int(input("Enter the principle of the simple interest : "))
time = float(input("Enter the time of the simple interest : "))
rate = float(input("Enter the rate of the simple interest : "))

# Without function...
# simple_interest = principle*time*rate/100

'''
# using define function

def simple_interest(p,t,r) : 
    return (p*t*r)/100

print(simple_interest(principle,time,rate))


'''

'''
using lambda function...

'''
'''

si = lambda p,t,r : (p*t*r)/100

p,t,r=principle,time,rate

print(si(p,t,r))

'''

# using list comprehension...

p,t,r = principle,time,rate

print([p*t*r/100][0])

