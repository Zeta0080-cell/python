def insert(a,size,j):
    i=size-1
    while i>=0 and j<=a[i]:
        a[i+1]=a[i]
        i-=1
    a[i+1]=j

size=4
a=[1,4,6,9]+[0]*16
j=int(input("请输入要插入的元素："))
insert(a,size,j)
for i in range(5):
    print(a[i],end="")