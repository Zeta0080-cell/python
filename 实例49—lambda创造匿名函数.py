#lambda是一个简化的函数，其可以快捷定义
#lambda 参数列表: 表达式
#实例： add = lambda x, y: x + y

MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print('The largar one is %d' % MAXIMUM(a, b))
    print('The lower one is %d' % MINIMUM(a, b))