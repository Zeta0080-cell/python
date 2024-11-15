def solution(n, m, q, arrayN, arrayQ):
    # 初始化结果列表
    result = []

    # 将每个用户的实验命中情况存储在集合中
    user_experiments = []
    for user in arrayN:
        # 提取用户命中的实验
        experiments = user[1:]
        # 将实验存储在集合中
        user_experiments.append(set(experiments))

    # 处理每次查询
    for query in arrayQ:
        # 提取查询的实验条件
        query_experiments = query[1:]
        # 初始化符合条件的用户数量
        count = 0

        # 遍历每个用户
        for user_set in user_experiments:
            # 检查用户是否符合查询条件
            if check_user_matches_query(user_set, query_experiments):
                count += 1

        # 将符合条件的用户数量添加到结果列表中
        result.append(count)

    return result


# 检查用户是否符合查询条件的函数
def check_user_matches_query(user_set, query_experiments):
    # 遍历查询中的每个实验条件
    for exp in query_experiments:
        # 如果实验条件是正数，检查用户是否命中该实验
        if exp > 0 and exp not in user_set:
            return False
        # 如果实验条件是负数，检查用户是否未命中该实验
        elif exp < 0 and -exp in user_set:
            return False
    # 如果所有条件都满足，返回 True
    return True


if __name__ == "__main__":
    # Add your test cases here

    print(
        solution(
            3,
            3,
            3,
            [[2, 1, 2], [2, 2, 3], [2, 1, 3]],
            [[2, 1, -2], [2, 2, -3], [2, 3, -1]],
        )
        == [1, 1, 1]
    )
