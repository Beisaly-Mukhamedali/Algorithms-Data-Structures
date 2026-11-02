import math
def primes_less_and_equal_than(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    if n < 2:
        return []
    for i in range(2, math.isqrt(n) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return sum(is_prime)

def main():
    n = int(input())
    print(primes_less_and_equal_than(n))

main()

def counting_leaves(root):
    if not root:
        return []
    return counting_leaves(root.left) + counting_leaves(root.right)