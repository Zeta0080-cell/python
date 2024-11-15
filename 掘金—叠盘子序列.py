def solution(plates: list[int], n: int) -> str:
    result = []
    current_sequence = []

    for i in range(n):
        # 如果当前序列是空的，或者当前盘子可以加入当前序列
        if not current_sequence or plates[i] == current_sequence[-1] + 1:
            current_sequence.append(plates[i])
        else:
            # 处理当前序列并重置
            if len(current_sequence) >= 3:
                result.append(f"{current_sequence[0]}-{current_sequence[-1]}")
            else:
                result.extend(map(str, current_sequence))
            current_sequence = [plates[i]]

    # 处理最后一个序列
    if len(current_sequence) >= 3:
        result.append(f"{current_sequence[0]}-{current_sequence[-1]}")
    else:
        result.extend(map(str, current_sequence))

    return ",".join(result)


if __name__ == "__main__":
    #  You can add more test cases here
    print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20], 10) == "-3--1,2,10,15,16,18-20")
    print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
                   20) == "-6,-3-1,3-5,7-11,14,15,17-20")
    print(solution([1, 2, 7, 8, 9, 10, 11, 19], 8) == "1,2,7-11,19")

