def GCD(x, y):
    x, y = max(x,y), min(x,y)
    while y:
        x, y = y, (x % y)
    return x