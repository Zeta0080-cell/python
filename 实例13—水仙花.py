for num in range(100, 1000):
    # 分解出个位、十位和百位
    digit1 = num // 100  # 百位
    digit2 = (num // 10) % 10  # 十位
    digit3 = num % 10  # 个位
    # 计算各位数字的立方和
    if digit1**3 + digit2**3 + digit3**3 == num:
        print(num)