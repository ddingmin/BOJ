# BOJ 1987

n, m = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우
arr = []
for i in range(n):
    arr.append(list(input()))

ans = 1
# dfs로 탐색하여 사용했던 알파벳은 passedAlpha 배열을 통해 1로 바꾸어 다시 사용하지 못하도록 함.
def dfs(i, j, a):
    global ans
    if a >= ans: ans = a
    passedAlpha[ord(arr[i][j])] = 1
    for k in range(4):
        x, y = i + dx[k], j + dy[k]
        flag = False
        if not(0 <= x < n and 0 <= y < m): continue
        if passedAlpha[ord(arr[x][y])] == 1: continue
        passedAlpha[ord(arr[x][y])] = 1
        dfs(x, y, a + 1)
        passedAlpha[ord(arr[x][y])] = 0

passedAlpha = [0] * 100
dfs(0, 0, 1)
print(ans)