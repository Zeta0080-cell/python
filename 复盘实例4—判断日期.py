def is_run(n):
    if n%400==0 or (n%4==0 and n%100!=0):
        return True

year=int(input("请输入年份："))
month=int(input("请输入月份："))
day=int(input("请输入日期："))
result=0
list1=[31,29,31,30,31,30,31,31,30,31,30,31]
list2=[31,28,31,30,31,30,31,31,30,31,30,31]
if is_run(year):
    for i in range(0,month-1):
        result+=list1[i]
    result+=day
else:
    for j in range(0,month-1):
        result+=list2[j]
    result+=day
print(result)
