def is_prime(n):
    for i in range(2, n + 1):
        if i != n and n % i == 0:
            return "NO"
    else:
        return "YES"

print(is_prime(int(input())))