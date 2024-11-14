#具体使用方法和与相同，查看51例
#规则：0|0=0; 0|1=1; 1|0=1; 1|1=1
if __name__ == '__main__':
    a = 0o77
    b = a | 3
    print ('a | b is %d' % b)
    b |= 7
    print ('a | b is %d' % b)