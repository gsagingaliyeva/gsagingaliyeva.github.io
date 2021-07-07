def is_prime(a):
    i=2
    Prime = "True" 
    while i<a:
        if a%i==0: 
            Prime = "False"
        i=i+1
    
    if a==1:
        Prime = "False"

    print (Prime)