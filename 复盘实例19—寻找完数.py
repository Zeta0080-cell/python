n=int(input("请输入你想要的整数n:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if n==sum:
    print("这是一个完数")