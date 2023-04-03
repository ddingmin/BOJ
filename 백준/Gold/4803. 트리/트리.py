import sys
import heapq
from collections import deque
from bisect import bisect_left
import math
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(case, n, m, adj):
    def bfs(start):
        q = deque()
        visit[start] = n + 1
        q.append(start)
        while q:
            cur = q.popleft()
            for next in adj[cur]:
                if not visit[next]:
                    visit[next] = cur
                    q.append(next)
                elif visit[cur] == next:
                    continue
                else:
                    return 0
        return 1
                
    visit = [0] * (n + 1)
    count = 0
    for i in range(1, n + 1):
        if not visit[i]:
            count += bfs(i)
    
    if count > 1:
        print(f"Case {case}: A forest of {count} trees.")
    elif count == 1:
        print(f"Case {case}: There is one tree.")
    else:
        print(f"Case {case}: No trees.")
            
    return count

# input
case = 1
while 1:
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    if (n, m) == (0, 0): break
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    solve(case, n, m, adj)
    case += 1
