import heapq

input = __import__('sys').stdin.readline

n = int(input())
me = int(input())

if n == 1:
    print(0)
    exit()

h = []
ans = 0
for i in range(1,n):
    heapq.heappush(h,-int(input()))
while me <= -h[0]:
    heapq.heappush(h, heapq.heappop(h) + 1)
    me += 1
    ans += 1
print(ans)
