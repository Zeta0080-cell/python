def solution(n: int, l: int, r: int, a: list) -> int:
    count = 0  # 初始化计数器
    for x in a:  # 遍历数组
        # 检查条件
        if x % 2 == 0 and l <= x <= r:
            count += 1  # 更新计数器
    return count  # 返回结果

if __name__ == '__main__':
    print(solution(5, 3, 8, [1, 2, 6, 8, 7]) == 2)
    print(solution(4, 10, 20, [12, 15, 18, 9]) == 2)
    print(solution(3, 1, 10, [2, 4, 6]) == 3)