def solution(nums):
    # 统计每个序号的棋子数量
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # 检查每个序号的棋子数量是否能被5整除
    for count in count_dict.values():
        if count % 5 != 0:
            return "False"

    return "True"
