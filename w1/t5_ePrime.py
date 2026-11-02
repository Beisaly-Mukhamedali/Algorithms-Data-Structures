def prime(n):
    p = 2
    arr = []
    while p * p <= n:
        while n % p == 0:
            arr.append(p)
            n //= p
        p += 1
    if n > 1:
        arr.append(n)
    return arr
print(*prime(int(input())))
