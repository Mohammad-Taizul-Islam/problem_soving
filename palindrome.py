#Naive Approach Palindorm

'''

def palindromChecker(str) :
    
    
    left = 0
    right = len(str)
    
    while left < right :
        if  str[left] != str[right-1] :
            return False
        left+=1
        right-=1
    
    return True

print(palindromChecker("ABBBA"))
    
'''


#using recursion...

'''

def isPalindromeUtil(s,left,right) :
    if left >= right :
        return True
    
    if s[left] != s[right] :
        return False
    return isPalindromeUtil(s,left+1,right-1)


def isPalindrome(s) :
    left = 0
    right = len(s) - 1
    
    return isPalindromeUtil(s,left,right)

s = "KAKA"
print(isPalindrome(s))

'''

#reversing the string...

'''
def isPalindrome(str) :
    return str == str[::-1]


while True :
    user_input = input("Enter a string for Palindrome checking : ").strip()
    print(isPalindrome(user_input))
    if user_input.lower == 'exit' :
        break
     

print(isPalindrome(user_input))

'''


#Using single variable...

def isPalindrome(s) :
    
    length = len(s)
    
    for i in range(length//2) :
        if s[i] !=s[length-i-1] :
            return False
        
    return True


while True :
    user_input = input("Enter a string for Palindrome checking : ").strip()
    print(isPalindrome(user_input))
    if user_input.lower == 'exit' :
        break
     

print(isPalindrome(user_input))




