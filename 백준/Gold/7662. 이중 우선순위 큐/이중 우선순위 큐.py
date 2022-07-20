import heapq

t = int(input())

def syn(arr):
    while arr and visit[arr[0][1]] == 0:
        heapq.heappop(arr)

for _ in range(t):
    hq = [] # 최소
    hq2 = [] # 최대
    visit = [0] * 1000000
    k = int(input())

    for i in range(k):
        n, m = map(str, input().split())
        if n == 'I':
            heapq.heappush(hq, (int(m), i))
            heapq.heappush(hq2, (-1 * int(m), i))
            visit[i] = 1

        elif m == '1':
            syn(hq2)
            if hq2:
                visit[hq2[0][1]] = 0
                heapq.heappop(hq2)
        else:
            syn(hq)
            if hq:
                visit[hq[0][1]] = 0
                heapq.heappop(hq)
    syn(hq2)
    syn(hq)


    if hq: print(-hq2[0][0], hq[0][0])
    else: print('EMPTY')
