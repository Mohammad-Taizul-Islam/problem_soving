#compound interest

principle = int(input("Enter the principle of the compound interest : "))
time = int(input("Enter the time of the simple interest : "))
rate = float(input("Enter the rate of the simple interest : "))

p,t,r = principle,time,rate

# Using Exponentiation Operator
# amount = p*(1+r/100)**t

# Build in 'pow' method...

# amount = p * pow((1+r/100),t)


#using for loop...


amount = p

for i in range(t) :
    amount = amount * (1+r/100)

ci = amount - p



print(f"Compound interest : {ci}") 