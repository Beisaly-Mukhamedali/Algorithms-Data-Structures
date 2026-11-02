import heapq

input()
a = input()
stones = [-int(x) for x in a.split()]
heapq.heapify(stones)

while len(stones) > 1:
    y = -heapq.heappop(stones)
    x = -heapq.heappop(stones)
    
    if y != x:
        heapq.heappush(stones, -(y - x))

if stones:
    print(-stones[0])
else:
    print(0)
