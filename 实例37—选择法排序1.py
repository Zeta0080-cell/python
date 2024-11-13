n=int(input("Enter a number:"))
a=[]

for i in range(n):
    element=int(input("请输入数组元素"))
    a.append(element)

for k in range(n-1):
    index=k
    for j in range(k+1,n):
        if a[j]<a[index]:
            index=j
    a[index],a[k]=a[k],a[index]

print("排列后的数组：",end="")
for i in range(n):
    print(a[i],end="")