def fibonacci_list(a):
    Fiblist=[1,1]
    while len (str(Fiblist[-1]))<a:
        Fiblist.append (Fiblist[-1]+Fiblist[-2])
    print (Fiblist[-1])
  
