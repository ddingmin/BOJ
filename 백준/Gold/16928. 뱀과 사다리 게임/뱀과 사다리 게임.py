from collections import deque

n, m = map(int, input().split())
go = [0] * 101
visit = [0] * 101
for i in range(n):
    a, b = map(int, input().split())
    go[a] = b
for i in range(m):
    a, b = map(int, input().split())
    go[a] = b

def bfs(x):
    q = deque()
    q.append((x, 1))
    visit[x] = 1
    while q:
        dir, ans = q.popleft()
        for k in range(1, 7):
            d = dir + k
            if d == 100: return ans
            if 1 <= d <= 100 and visit[d] == 0:
                if go[d] != 0: d = go[d]
                visit[d] = 1
                q.append((d, ans + 1))

print(bfs(1))
