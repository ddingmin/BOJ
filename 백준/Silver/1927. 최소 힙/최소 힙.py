import heapq

input = __import__('sys').stdin.readline

n = int(input())
h = []
for i in range(n):
    t = int(input())
    if t == 0:
        if h: print(heapq.heappop(h))
        else: print(0)
    else:
        heapq.heappush(h, t)