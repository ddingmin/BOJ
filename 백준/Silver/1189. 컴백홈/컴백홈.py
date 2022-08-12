input = __import__('sys').stdin.readline

# input
r, c, dist  = map(int, input().split())
arr = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(r):
    arr.append(list(input().strip()))

ans = 0

def dfs(depth, i, j):
    global ans
    
    if depth == dist:
        if (i == 0 and j == c - 1):
            ans += 1
            return
        else:
            return
    if i == 0 and j == c - 1: return
    
    for k in range(4):
        x, y = i + dx[k], j + dy[k]
        if not(0 <= x < r and 0 <= y < c): continue
        if arr[x][y] == 'a' or arr[x][y] == 'T': continue
        arr[x][y] = 'a'
        dfs(depth + 1, x, y)
        arr[x][y] = '.'
        
arr[r - 1][0] = 'a'
dfs(1, r - 1, 0)
print(ans)
        