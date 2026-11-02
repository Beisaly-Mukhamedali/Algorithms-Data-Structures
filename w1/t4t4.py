def nthPrime(n):
    count = 0
    p = 2
    while True:
        for i in range(2,p):
            if p % i == 0 and i != p:
                break
        else:
            count += 1
        if count == n:
            return p
        p += 1

print(nthPrime(5))