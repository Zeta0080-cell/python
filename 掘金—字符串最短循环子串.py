def solution(inp):
    # 遍历所有可能的子串长度
    for length in range(1, len(inp) // 2 + 1):
        # 提取子串
        substring = inp[:length]
        # 检查是否可以通过重复该子串来构成原字符串
        if substring * (len(inp) // length) == inp:
            return substring
    # 如果没有找到符合条件的子串，返回空字符串
    return ""

if __name__ == "__main__":
    # 添加你的测试用例
    print(solution("abcabcabcabc") == "abc")
    print(solution("aaa") == "a")
    print(solution("abababab") == "ab")
    print(solution("ab") == "")
    print(solution("abcdabcdabcdabcd") == "abcd")
    print(solution("b") == "")
