#要求使用datetime模块来输出指定格式的日期
#if __name__ == '__main__': 是Python中的一个常用模式，用于判断当前脚本是否作为主程序运行。这个模式非常有用，因为它允许你的Python文件既可以作为脚本直接运行，也可以作为模块被其他Python文件导入。
#在Python中，每个模块都有一个__name__变量，当模块被直接运行时，__name__的值会被设置为'__main__'。如果模块是被导入的，那么__name__的值会被设置为模块的名字。
#作为主程序运行：当你直接运行一个Python文件时，Python解释器会将__name__设置为'__main__'。因此，if __name__ == '__main__': 这个条件会被满足，代码块内的代码会被执行。
#作为模块导入：当你将一个Python文件作为模块导入到另一个Python文件中时，__name__会被设置为该模块的名字。例如，如果你有一个名为module.py的文件，当你在另一个文件中使用import module导入它时，module.__name__会被设置为'module'。在这种情况下，if __name__ == '__main__': 这个条件不会被满足，代码块内的代码不会被执行。
#这种模式的好处是，你可以在同一个文件中编写既可以作为模块被导入和使用，也可以作为独立程序运行的代码.

import datetime

if __name__ == '__main__':
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%d/%m/%Y'))

    # 创建日期对象
    miyazakiBirthDate = datetime.date(1941, 1, 5)

    print(miyazakiBirthDate.strftime('%d/%m/%Y'))

    # 日期算术运算
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)

    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

    # 日期替换
    miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)

    print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))
