def Perfect(num):
    sum=0
    for i in range(1,num):
        if num % i == 0:
            sum+=i
            if sum==num:
                return True

for num in (1,1001):
    if Perfect(num):
        print(num,end="")