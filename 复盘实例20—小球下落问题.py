item=float(50)
result=0
height=float(100)
flag=float(0)
for i in range(1,10):
    flag=flag+item
    item/=2
result=height+2*flag
print(result)
