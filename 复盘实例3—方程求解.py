for i in range(1,168//2+1):
    if 168%i==0:
        j=168/i
        if (i+j)%2==0 and (i-j)%2==0 and i>j:
            m=(i+j)//2
            n=(i-j)//2
            x=n*n-100
            print("%d"%x)