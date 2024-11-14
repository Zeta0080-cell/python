a=[]
n=int(input("n:"))
for i in range(n):
    a.append([])
    for j in range(i+1):
        if j==0 or j==i:
            a[i].append(1)
        else:
            a[i].append(a[i-1][j]+a[i-1][j-1])
for i in a:print(i)