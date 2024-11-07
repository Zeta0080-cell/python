def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 输入要计算的斐波那契数列的项
n = int(input("请输入要计算的斐波那契数列的项数: "))

print(f"斐波那契数列的第 {n} 项是: {fib(n)}")