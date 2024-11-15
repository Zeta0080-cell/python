def solution(a: int, b: int) -> int:
    # 将数字 a 和 b 转换为字符串
    str_a = str(a)
    str_b = str(b)

    # 初始化最大结果为插入到最前面的情况
    max_result = int(str_b + str_a)

    # 遍历字符串 a 的每一个位置
    for i in range(len(str_a) + 1):
        # 尝试将 str_b 插入到位置 i
        new_str = str_a[:i] + str_b + str_a[i:]

        # 将新字符串转换为整数
        new_num = int(new_str)

        # 比较并更新最大结果
        if new_num > max_result:
            max_result = new_num

    return max_result


if __name__ == '__main__':
    print(solution(76543, 4) == 765443)
    print(solution(1, 0) == 10)
    print(solution(44, 5) == 544)
    print(solution(666, 6) == 6666)