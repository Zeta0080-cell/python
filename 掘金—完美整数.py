def solution(x, y):
    count = 0
    for num in range(x, y + 1):
        # 将整数转换为字符串
        num_str = str(num)
        # 检查字符串中的所有字符是否相同
        if all(char == num_str[0] for char in num_str):
            count += 1
    return count

if __name__ == "__main__":
    print(solution(1, 10) == 9)
    print(solution(2, 22) == 10)