def solution(s: str) -> int:
    # 将字符串转换为小写，以便忽略大小写
    s = s.lower()

    # 统计字符 'k' 和 'u' 的出现次数
    count_k = s.count('k')
    count_u = s.count('u')

    # 返回 'k' 和 'u' 出现次数的最小值
    return min(count_k, count_u)


if __name__ == '__main__':
    print(solution("AUBTMKAxfuu") == 1)
    print(solution("KKuuUuUuKKKKkkkkKK") == 6)
    print(solution("abcdefgh") == 0)