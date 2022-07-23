from collections import deque
f, s, g, u, d = map(int, input().split())
dir = [u, -d]
visit = [0] * (f + 1)
def bfs(g, s):
    ans = 0
    q = deque()
    q.append((s, ans))
    while q:
        temp, ans = q.popleft()
        if temp == g: return ans
        for k in range(2):
            s = temp + dir[k]
            if not(0 < s < len(visit)): continue
            if visit[s] == 1: continue
            q.append((s, ans + 1))
            visit[s] = 1
    return "use the stairs"

print(bfs(g, s))