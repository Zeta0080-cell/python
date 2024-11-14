def main():
    # 获取数组元素的个数
    n = int(input("请输入数组元素的个数："))
    a = []  # 创建一个空列表来存储数组元素

    for i in range(n):
        a.append(int(input()))  # 读取每个元素并添加到列表中

    # 将最大的元素交换到第一个位置
    for i in range(n):
        max_val = a[i]  # 假设当前元素是最大的
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > max_val:
                max_val = a[j]  # 更新最大值
                max_idx = j
        # 交换最大值到当前的位置
        a[i], a[max_idx] = a[max_idx], a[i]

    # 将最小的元素交换到最后一个位置
    for i in range(n - 1, -1, -1):
        min_val = a[i]  # 假设当前元素是最小的
        min_idx = i
        for j in range(i - 1, -1, -1):
            if a[j] < min_val:
                min_val = a[j]  # 更新最小值
                min_idx = j
        # 交换最小值到当前位置
        a[i], a[min_idx] = a[min_idx], a[i]

    # 输出排序后的数组元素
    for i in range(n):
        print(a[i], end=' ')  # 输出排序后的数组元素
    print()

if __name__ == "__main__":
    main()