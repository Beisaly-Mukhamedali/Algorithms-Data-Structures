import sys

def compute_hash(s):
    MOD = 10**9 + 7
    h = 0
    p = 1
    for i, char in enumerate(s):
        val = ord(char) - 47
        h = (h + ((val % MOD) * p) % MOD) % MOD
        p = (p * 11) % MOD
    return h

def main():
    lines = sys.stdin.read().splitlines()
    n = int(lines[0])
    items = lines[1:2 * n + 1]
    counts = {}

    for x in items:
        counts[x] = counts.get(x, 0) + 1

    for s_str in items:
        if counts[s_str] == 0:
            continue

        h_str = str(compute_hash(s_str))

        if s_str == h_str:
            if counts[s_str] >= 2:
                counts[s_str] -= 2
                print(f'Hash of string "{s_str}" is {h_str}')
        else:
            if counts.get(h_str, 0) > 0:
                counts[s_str] -= 1
                counts[h_str] -= 1
                print(f'Hash of string "{s_str}" is {h_str}')

main()