n=int(input("请输入数组元素的个数："))
a=[]
for i in range(n):
    a.append(int(input("请输入数组的元素：")))

for k in range(0,n-1):
    index=k
    for i in range(k+1,n):
        if a[i]<a[index]:
            index=i
    temp=a[index]
    a[index]=a[k]
    a[k]=temp

for i in range(0,n):
    print(a[i])