if d<=10:
        tot=2**d
        print(tot)
    else:
        
        x=(2**10)*3**(d-10)
        if x>n:
            print(n)
        else:
            print(x)
