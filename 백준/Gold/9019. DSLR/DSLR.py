from collections import deque

visit = [0] * 10000

def dslr(x, value):
    if x == 0: # d
        value *= 2
        if value > 9999: value %= 10000
        return value
    elif x == 1: # s
        if value == 0: value = 9999
        else: value -= 1
        return value
    elif x == 2: # l
        temp = (value % 1000) * 10 + (value // 1000)
        return temp
    else: # r
        temp = value // 10 + 1000 * (value % 10)
        return temp

def bfs(value, equ):
    q = deque()
    q.append((value, ''))
    visit[value] = 1
    while q:
        v, a = q.popleft()
        if int(v) == int(equ): return a
        for k in range(4):
            val = dslr(k, v)
            if visit[val] == 0:
                if k == 0: ans = a + "D"
                elif k == 1: ans = a + "S"
                elif k == 2: ans = a + "L"
                elif k == 3: ans = a + "R"
                q.append((val, ans))
                visit[val] = 1

t = int(input())
for k in range(t):
    visit = [0] * 10000
    s, equ = map(int, input().split())
    print(bfs(s, equ))

