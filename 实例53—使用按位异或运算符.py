#规则：0^0=0; 0^1=1; 1^0=1; 1^1=0
if __name__ == '__main__':
    a = 0o77
    b = a ^ 3
    print ('The a ^ 3 = %d' % b)
    b ^= 7
    print ('The a ^ b = %d' % b)