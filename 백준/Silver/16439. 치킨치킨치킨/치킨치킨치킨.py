from itertools import combinations as cb

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i, j, k in cb(range(m), 3):
    temp = 0
    for idx in range(n):
        temp += max(arr[idx][i], arr[idx][j], arr[idx][k])
    ans = max(ans, temp)

print(ans)
            