import sys
from collections import deque
input = sys.stdin.readline

def solve(n, adj):
    visit = [0] * (n + 1)
    answer = [0] * (n + 1)

    q = deque()
    q.append(1)
    visit[1] = 1

    while q:
        cur = q.popleft()
        for next in adj[cur]:
            if visit[next] == 0:
                visit[next] = 1
                answer[next] = cur
                q.append(next)

    return answer[2:]

n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

print("\n".join(map(str, solve(n, adj))))