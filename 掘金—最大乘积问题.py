def solution(n, array):
    # 初始化 L 和 R 数组
    L = [0] * n
    R = [0] * n

    # 计算 L(i)
    stack = []
    for i in range(n):
        while stack and array[stack[-1]] <= array[i]:
            stack.pop()
        if stack:
            L[i] = stack[-1] + 1  # 因为题目中下标从1开始
        stack.append(i)

    # 计算 R(i)
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and array[stack[-1]] <= array[i]:
            stack.pop()
        if stack:
            R[i] = stack[-1] + 1  # 因为题目中下标从1开始
        stack.append(i)

    # 计算 MAX(i) 并找出最大值
    max_product = 0
    for i in range(n):
        max_product = max(max_product, L[i] * R[i])

    return max_product


if __name__ == "__main__":
    print(solution(5, [5, 4, 3, 4, 5]) == 8)
    print(solution(6, [2, 1, 4, 3, 6, 5]) == 15)
    print(solution(7, [1, 2, 3, 4, 5, 6, 7]) == 0)