import math
def is_shuixianhua(n):
    origin = n
    sum=0
    while n !=0:
        digit=n%10
        sum+=pow(digit,3)
        n=n//10
    if sum==origin:
        return True

for i in range(100,1000):
    if is_shuixianhua(i):
        print(i)