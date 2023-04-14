import sys
import heapq
import math
from collections import deque
from bisect import bisect_left
input = sys.stdin.readline

def solve(n, adj):
    scores = []
    # 점수, 회원 번호
    for start in range(1, n + 1):
        visit = [0] * (n + 1)
        q = deque()
        q.append(start)
        visit[start] = 1
        score = -1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                for next in adj[cur]:
                    if visit[next] == 0:
                        visit[next] = 1
                        q.append(next)
            score += 1
        scores.append([score, start])
    
    scores.sort()
    answer = [scores[0][1]]
    for i in range(1, n):
        if scores[i][0] == scores[0][0]:
            answer.append(scores[i][1])
    print(scores[0][0], len(answer))
    print(*sorted(answer))


n = int(input())
adj = [[] for _ in range(n + 1)]
while 1:
    a, b = map(int, input().split())
    if a == -1 and b == -1: break
    adj[a].append(b)
    adj[b].append(a)

solve(n, adj)