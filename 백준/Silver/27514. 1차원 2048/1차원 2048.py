import sys
import heapq
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

hq = []
for i in nums:
    heapq.heappush(hq, i)

ans = 0
answer = 0
while hq:
    ans = max(ans, hq[0])
    if hq[0] == 0:
        heapq.heappop(hq)
    elif hq[0] == answer:
        heapq.heappop(hq)
        heapq.heappush(hq, answer * 2)
        answer = 0
    else:
        answer = heapq.heappop(hq)
print(answer)