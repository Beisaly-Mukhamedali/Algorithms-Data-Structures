def factorization(n):
    p = 2
    result = []
    while p * p <= n:
        while n % p == 0:
            result.append(p)
            n //= p
        p += 1
    if n > 1:
        result.append(n)
    return result

n = int(input())

print(*factorization(n))