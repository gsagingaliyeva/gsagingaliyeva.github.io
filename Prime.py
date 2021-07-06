def is_prime(a):
    n=a
    Prime=[2,3,5,7,11]
    if n<=1: 
        print ("False")
    elif n in Prime:
        print ("True")
    elif n not in Prime and n%2==0 or n%3==0 or n%4==0 or n%5==0 or n%6==0 or n%7==0 or n%8==0 or n%9==0:
        print ("False")
    else:
        print ("True")