#兔子数列
def rabbit_population(n):
    # 创建一个数组用于保存每个月的兔子数量
    if n <= 2:
        return 1
    # 初始化前两个月的兔子数
    a, b = 1, 1
    for month in range(3, n + 1):
        a, b = b, a + b
    return b

# 输入月份数
n = int(input("请输入要计算的月份数："))
print(f"{n}个月后的兔子总数为：{rabbit_population(n)}")