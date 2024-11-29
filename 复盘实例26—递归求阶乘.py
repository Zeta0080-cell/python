def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

n=int(input("请输入你想求阶乘的数字："))
print(fact(n))