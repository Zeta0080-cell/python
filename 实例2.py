i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for j in range(0,6):
    if i>arr[j]:
        r+=(i-arr[j])*rat[j]
        print ((i-arr[j])*rat[j])
        arr[j] = i
print (r)