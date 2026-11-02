import heapq

input()
arr = list(map(int, input().split()))
heap = arr[:]
heapq.heapify(heap)
if heap == arr:
    print("YES")
else:
    print("NO")