import sys
from collections import deque


def filled(start, visit, adj):
    q = deque([start])
    visit[start] = 1

    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if visit[nxt]: continue
            visit[nxt] = 1
            q.append(nxt)
    return start


def solve(n, adj):
    visit = [0] * (n + 1)
    ans = []
    for i in range(1, n + 1):
        if visit[i]: continue
        ans.append(filled(i, visit, adj))
    return ans


def main():
    n = int(input())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 2):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    print(*solve(n, adj))


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 5)
    input = sys.stdin.readline
    main()
