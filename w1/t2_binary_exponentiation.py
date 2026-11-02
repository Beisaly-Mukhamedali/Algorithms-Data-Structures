def binpow(a,n,m):
    if n == 0:
        return 1 % m
    if n % 2 == 0:
        half = binpow(a, n // 2, m)
        return half * half % m
    else:
        return a * binpow(a, n - 1, m) % m

a, n, m = map(int, input().split()) 

print(binpow(a, n, m))