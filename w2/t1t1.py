from collections import deque, Counter

n = int(input())
results = []
for _ in range(n):
    input()
    stream = input().split()
    freq = Counter()
    q = deque()
    result = []
    for char in stream:
        freq[char] += 1
        q.append(char)
        while q and freq[char] > 1:
            q.popleft()
        if q:
            result.append(q[0])
        else:
            result.append("-1")
    results.append(result)

for h in results:
    print(*h)