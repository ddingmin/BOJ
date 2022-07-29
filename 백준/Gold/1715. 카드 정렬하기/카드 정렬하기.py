import heapq
input = __import__('sys').stdin.readline

n = int(input())
hq = []
ans = 0

for _ in range(n):
    heapq.heappush(hq, int(input()))
    
while len(hq) > 1:
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    ans += a + b
    heapq.heappush(hq, a + b)

print(ans)