def solution(A):
    if A == 1:
        return 1
    elif A == 2:
        return 2

    # 初始化前两项的值
    a, b = 1, 2

    # 从第3个月开始计算
    for _ in range(3, A + 1):
        # 计算新的兔子对数
        c = a + b
        # 更新前两项的值
        a, b = b, c

    return b


if __name__ == "__main__":
    # Add your test cases here
    print(solution(5) == 8)
    print(solution(1) == 1)
    print(solution(15) == 987)
    print(solution(50) == 20365011074)
