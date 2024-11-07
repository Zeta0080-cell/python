def runnian(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def day_of_year(year, month, day):
    """返回给定日期是这一年的第几天"""
    # 每个月的天数，默认是非闰年
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 如果是闰年，修改2月的天数
    if runnian(year):
        days_in_month[1] = 29  # 闰年的2月有29天

    # 计算前几个月的天数总和
    days_before_month = sum(days_in_month[:month - 1])

    # 加上当前月份的天数
    return days_before_month + day


year = int(input("请输入年份: "))
month = int(input("请输入月份: "))
day = int(input("请输入日期: "))

# 计算并输出该日期是这一年的第几天
result = day_of_year(year, month, day)
print(f"{result}")