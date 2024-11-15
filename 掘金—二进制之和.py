def solution(binary1, binary2):
    # 将二进制字符串转换为十进制整数
    decimal1 = int(binary1, 2)
    decimal2 = int(binary2, 2)

    # 计算两者的和
    decimal_sum = decimal1 + decimal2

    # 将结果转换为十进制字符串返回
    return str(decimal_sum)


if __name__ == "__main__":
    #  You can add more test cases here
    print(solution("101", "110") == "11")
    print(solution("111111", "10100") == "83")
    print(solution("111010101001001011", "100010101001") == "242420")
    print(solution("111010101001011", "10010101001") == "31220")