sum=0
item=0
n=int(input("请输入相加数的个数："))
a=int(input("请输入你想相加的数："))
for i in range(1,n+1):
    sum=sum+item
    item=item*10+a
print(sum)