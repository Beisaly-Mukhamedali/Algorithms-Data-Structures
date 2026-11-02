def prime(n):
    p = 2
    count = 0
    while True:
        for i in range(2, p + 1):
            if p % i == 0 and i != p:
                break
        else:
            count += 1
        if count == n:
            return p
        p += 1

print(prime(int(input())))
