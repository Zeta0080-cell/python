n = int(input("请输入n的值:"))
k = 2
while n != 1:
    while n % k ==0:
        print("%d"%k,sep="",end="")
        n=n/k
        if n!=1:
            print("*",end="")
    k=k+1