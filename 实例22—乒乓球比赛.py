for a in['x','y','z']:
    for b in ['x','y','z']:
        for c in ['x','y','z']:
            if(a!='x')and(b!='x')and(c!='z')and(a!=b)and(b!=c)and(c!=a):
                print("a--%c b--%c c--%c"%(a,b,c))
