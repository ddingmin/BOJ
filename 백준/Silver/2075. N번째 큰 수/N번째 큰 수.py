import heapq
n = int(input())
hq = []
for i in range(n):
    temp = list(map(int, input().split()))
    for k in range(n):
        if i == 0:
            heapq.heappush(hq, -1 * temp[k])
            hq = sorted(hq)
        else:
            if hq[n-1] > -1 * temp[k]:
                hq.pop()
                heapq.heappush(hq, -1 * temp[k])
                hq = sorted(hq)

print(-1 * hq[n-1])