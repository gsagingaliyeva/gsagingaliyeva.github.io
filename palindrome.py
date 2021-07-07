def is_palindrome(a):
    b=str(a)
    if b[0]==b[-1] and b[1]==b[-2]:
        return "True"
    else:
        return "False"
    
def is_prime(a):
    i=2
    Prime = "True" 
    while i<a:
        if a%i==0: 
            Prime = "False"
        i=i+1
    
    if a==1:
        Prime = "False"

    return Prime

def is_palindrome_primes():
    PalindromePrime = []
    i=10000
    while i>=10000 and i<=99999:
        if is_palindrome(i)=="True" and is_prime(i)=="True":
            PalindromePrime.append(i)

        i=i+1
    
    print (PalindromePrime)

