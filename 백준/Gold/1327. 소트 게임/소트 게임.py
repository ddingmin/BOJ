from collections import deque
from itertools import permutations



def solve(n, k, target):
    visit = [False] * (10 ** 6)
    temp = []    
    for i in range(1, n + 1):
        temp.append(i)
        
    match = {}
    chmat = {}
    idx = 0
    for i in permutations(temp, n):
        match[idx] = i
        chmat[i] = idx
        if list(i) == target: target = idx
        idx += 1
        

    def bfs(temp):
        q = deque()
        q.append(temp)
        visit[temp] = True
        count = 0
        
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target: return count
                for i in range(n - k + 1):
                    c = match[cur]
                    next = chmat[c[:i] + c[i: i + k][::-1] + c[i + k:]]
                    if visit[next] == False:
                        visit[next] = True
                        q.append(next)
            count += 1
        return -1

    return bfs(0)

n, k = map(int, input().split())
target = list(map(int, input().split()))
print(solve(n, k, target))