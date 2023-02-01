from collections import deque
mem = [-1] * 1_000_001

def cal(num, n, i):
    if i == 0: 
        return num + n
    elif i == 1: 
        return num * 2
    return num * 3

def bfs(num, y, n):
    q = deque()
    q.append(num)
    mem[num] = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            for i in range(3):
                nxt = cal(cur, n, i)
                if not (1 <= nxt < 1_000_001): 
                    continue
                if mem[nxt] == -1:
                    mem[nxt] = mem[cur] + 1
                    q.append(nxt)
                elif mem[nxt] > mem[cur] + 1:
                    mem[nxt] = mem[cur] + 1
                    q.append(nxt)
    return
            

def solution(x, y, n):
    mem[x] = 0
    bfs(x, y, n)
    answer = mem[y]
    return answer