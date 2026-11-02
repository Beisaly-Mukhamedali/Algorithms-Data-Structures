def computeGCD(x, y):
    x, y = max(x, y), min(x, y)
    while y:
        x, y = y, (x % y)
    return x

print(computeGCD(49, 70))
