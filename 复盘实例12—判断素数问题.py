import math
def is_sushu(n):
    if n<=1:
        return False
    elif n==2 or n==3:
        return True
    else:
        for i in range(2, math.isqrt(n) + 2):
            if n % i == 0:
                return False
        return True

n=int(input("请输入你想判断的数："))
for i in range(1,n+1):
    if is_sushu(i):
        print(i)