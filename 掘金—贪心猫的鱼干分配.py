def solution(n, cats_levels):
    # 步骤1：每只猫至少分配 1 斤鱼干
    fish_dry = [1] * n

    # 步骤2：从左往右遍历
    for i in range(1, n):
        if cats_levels[i] > cats_levels[i - 1]:
            fish_dry[i] = fish_dry[i - 1] + 1

    # 步骤3：从右往左遍历
    for i in range(n - 2, -1, -1):
        if cats_levels[i] > cats_levels[i + 1]:
            fish_dry[i] = max(fish_dry[i], fish_dry[i + 1] + 1)

    # 步骤4：计算总的鱼干数量
    return sum(fish_dry)

if __name__ == "__main__":
    #  You can add more test cases here
    cats_levels1 = [1, 2, 2]
    cats_levels2 = [6, 5, 4, 3, 2, 16]
    cats_levels3 = [1, 2, 2, 3, 3, 20, 1, 2, 3, 3, 2, 1, 5, 6, 6, 5, 5, 7, 7, 4]
    print(solution(3, cats_levels1) == 4)
    print(solution(6, cats_levels2) == 17)
    print(solution(20, cats_levels3) == 35)