def solution(n, b, sequence):
    # 初始化一个哈希表来记录前缀和的余数
    remainder_count = {}
    # 初始化前缀和
    prefix_sum = 0
    # 初始化结果计数器
    result = 0

    # 遍历序列中的每个元素
    for num in sequence:
        # 更新前缀和
        prefix_sum += num

        # 计算当前前缀和的余数
        remainder = prefix_sum % b

        # 如果余数为0，说明从序列开始到当前位置的和是b的倍数
        if remainder == 0:
            result += 1

        # 如果哈希表中已经有这个余数，说明存在一个子序列的和是b的倍数
        if remainder in remainder_count:
            result += remainder_count[remainder]

        # 更新哈希表中当前余数的计数
        if remainder in remainder_count:
            remainder_count[remainder] += 1
        else:
            remainder_count[remainder] = 1

    return result


if __name__ == "__main__":
    # 你可以添加更多测试用例
    sequence = [1, 2, 3]
    print(solution(3, 3, sequence) == 3)