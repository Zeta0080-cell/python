def octal_to_decimal(octal_str):
    # int()函数的第二个参数是基数，8表示八进制
    decimal_value = int(octal_str, 8)
    return decimal_value

# 示例调用
octal_str = input("请输入一个八进制数: ")
result = octal_to_decimal(octal_str)
print("对应的十进制数是:", result)