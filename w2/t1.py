from collections import deque, Counter

t = int(input())
results = []
for _ in range(t):
    input()
    stream = input().split()
    freq = Counter()
    q = deque()
    ans = []
    for char in stream:
        freq[char] += 1
        q.append(char)
        while q and freq[q[0]] > 1:
            q.popleft()
        if q:
            ans.append(q[0])
        else:
            ans.append("-1")
    results.append(ans)

for h in results:
    print(*h)
    