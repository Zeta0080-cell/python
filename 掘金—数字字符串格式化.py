def solution(s: str) -> str:
    # 去除前导零
    s = s.lstrip('0')
    if s == '':
        s = '0'

    # 分离整数和小数部分
    if '.' in s:
        integer_part, decimal_part = s.split('.')
    else:
        integer_part, decimal_part = s, ''

    # 格式化整数部分
    integer_part = integer_part[::-1]  # 反转字符串
    formatted_integer_part = ','.join([integer_part[i:i + 3] for i in range(0, len(integer_part), 3)])[::-1]

    # 合并整数和小数部分
    if decimal_part:
        return f"{formatted_integer_part}.{decimal_part}"
    else:
        return formatted_integer_part


if __name__ == '__main__':
    print(solution("1294512.12412") == '1,294,512.12412')
    print(solution("0000123456789.99") == '123,456,789.99')
    print(solution("987654321") == '987,654,321')