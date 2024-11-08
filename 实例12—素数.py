def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

prime_count = 0
print("101到200之间的素数有:")
for i in range(101, 201):
    if is_prime(i):
        print(i, end=' ')
        prime_count += 1
print("\n总共有{}个素数。".format(prime_count))
