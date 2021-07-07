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

def is_primebelow(a):
    Primebelow = []
    i=2
    while i<a:
        if is_prime(i)== "True":
            Primebelow.append (i)
        
        i=i+1
    
    print (Primebelow)

