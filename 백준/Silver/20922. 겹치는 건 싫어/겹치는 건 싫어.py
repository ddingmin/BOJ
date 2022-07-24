n, k = map(int, input().split())
arr = list(map(int, input().split()))
visit = [0] * 100001
l, r = 0, 0
cnt = 1
visit[arr[0]] = 1
ans = 0
while 1:
    if visit[arr[r + 1]] + 1 <= k:
        r += 1
        visit[arr[r]] += 1
        cnt += 1
    else:
        while visit[arr[r + 1]] + 1 > k:
            visit[arr[l]] -= 1
            l += 1
            cnt -= 1
        r += 1
        visit[arr[r]] += 1
        cnt += 1
    ans = max(ans, cnt)
    if r == n - 1: break
print(ans)
