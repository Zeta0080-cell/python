def solution(dna1, dna2):
    m, n = len(dna1), len(dna2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # 状态转移
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i - 1] == dna2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[m][n]


if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("AGT", "AGCT") == 1)
    print(solution("", "ACGT") == 4)
    print(solution("GCTAGCAT", "ACGT") == 5)