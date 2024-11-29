sum=0
a=int(input("请输入你想要的a的值："))
n=int(input("请输入你想要相加的项数："))
item=a
for i in range(1,n+1):
    sum=sum+item
    item=item*10+a
print(sum)