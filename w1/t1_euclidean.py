def computeGCD(x, y):
    x, y = max(x,y), min(x,y)
    while(y):
        x, y = y, (x % y)
    return x

num1, num2 = map(int, input().split())

print("GCD of {}, {} is {}".format(num1, num2, computeGCD(num1, num2)))