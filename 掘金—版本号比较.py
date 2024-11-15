def solution(version1, version2):
    # 将版本号按点号分割成修订号的列表
    v1_parts = version1.split('.')
    v2_parts = version2.split('.')

    # 获取两个版本号的修订号数量
    len1 = len(v1_parts)
    len2 = len(v2_parts)

    # 补齐修订号，使两个版本号的修订号数量相同
    max_len = max(len1, len2)
    v1_parts += ['0'] * (max_len - len1)
    v2_parts += ['0'] * (max_len - len2)

    # 逐个比较修订号
    for i in range(max_len):
        # 将修订号转换为整数进行比较
        v1_num = int(v1_parts[i])
        v2_num = int(v2_parts[i])

        if v1_num > v2_num:
            return 1
        elif v1_num < v2_num:
            return -1

    # 如果所有修订号都相等，返回0
    return 0


if __name__ == "__main__":
    # Add your test cases here
    print(solution("0.1", "1.1") == -1)
    print(solution("1.0.1", "1") == 1)
    print(solution("7.5.2.4", "7.5.3") == -1)
    print(solution("1.0", "1.0.0") == 0)
