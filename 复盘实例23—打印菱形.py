def print_diamond(rows):
    # 上半部分
    for i in range(1, rows, 2):
        spaces = " " * ((rows - i) // 2)
        stars = "*" * i
        print(spaces + stars)

    # 下半部分
    for i in range(rows, 0, -2):
        spaces = " " * ((rows - i) // 2)
        stars = "*" * i
        print(spaces + stars)

# 设置行数，可以根据需要调整
rows = 7
print_diamond(rows)