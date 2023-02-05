def sol(n, arr):
    # 초기 세팅
    dist =[[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]: dist[i][j] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j]: continue
                elif (dist[i][k] == 1 and dist[k][j] == 1): dist[i][j] = 1

    return dist

# input
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = (sol(n, arr))
for k in ans:
    print(*k)