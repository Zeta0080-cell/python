import math


def solution(x: int, y: int) -> int:
    distance = math.sqrt(x ** 2 + y ** 2)

    # 根据距离确定得分
    if distance <= 1:
        return 10
    elif distance <= 2:
        return 9
    elif distance <= 3:
        return 8
    elif distance <= 4:
        return 7
    elif distance <= 5:
        return 6
    elif distance <= 6:
        return 5
    elif distance <= 7:
        return 4
    elif distance <= 8:
        return 3
    elif distance <= 9:
        return 2
    elif distance <= 10:
        return 1
    else:
        return 0


if __name__ == '__main__':
    print(solution(1, 0) == 10)
    print(solution(1, 1) == 9)
    print(solution(0, 5) == 6)
    print(solution(3, 4) == 6)