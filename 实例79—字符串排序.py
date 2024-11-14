def sort_string(s):
    # 使用sorted()函数排序返回一个新的排序后的列表
    sorted_string = ''.join(sorted(s))
    return sorted_string

# 示例调用
s = input("请输入一个字符串: ")
result = sort_string(s)
print("排序后的字符串:", result)