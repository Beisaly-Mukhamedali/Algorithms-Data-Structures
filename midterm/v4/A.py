import math
a, b = map(int, input().split())
print(str(math.gcd(a,b)) + " " + str(math.lcm(a,b)))