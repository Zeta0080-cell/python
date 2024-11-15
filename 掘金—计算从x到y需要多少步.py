def solution(x, y):
    # 计算两个位置的距离
    d = abs(x - y)

    # 初始化变量
    step = 0  # 当前总步数
    move = 0  # 当前步长
    total_distance = 0  # 当前走过的总距离

    # 不断增加步长，直到走的距离大于等于 d
    while total_distance < d:
        step += 1  # 增加一步
        move = (step + 1) // 2  # 每两个步数，步长增加1
        total_distance += move

    return step