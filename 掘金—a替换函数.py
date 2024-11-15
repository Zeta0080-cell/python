def solution(s: str) -> str:
    # 使用replace方法将字符串中的小写字母'a'替换为'%100'
    # 注意：replace方法不会修改原字符串，而是返回一个新的字符串
    result = s.replace('a', '%100')

    # 返回替换后的字符串
    return result


if __name__ == '__main__':
    print(solution(s="abcdwa") == '%100bcdw%100')
    print(solution(s="banana") == 'b%100n%100n%100')
    print(solution(s="apple") == '%100pple')