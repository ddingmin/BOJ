# from collections import deque
import heapq


input = __import__('sys').stdin.readline
import heapq

# input
hq = []
hqq = []

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for k in arr:
    heapq.heappush(hq, -1 * k)
    
for b in arr2:
    a = -1 * heapq.heappop(hq)
    if a - b > 0: heapq.heappush(hq, (a - b) * -1)
    elif a - b < 0: 
        print(0)
        exit(0)
print(1)