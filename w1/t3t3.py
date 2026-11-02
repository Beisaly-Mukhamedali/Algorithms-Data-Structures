def isPrime(n):
    p = 2
    if n == 1:
        return "NO"
    while p * p <= n:
        if n % p == 0 and p != n:
            return "NO"
        p += 1
    else:
        return "YES"

n = int(input())
print(isPrime(n))
        