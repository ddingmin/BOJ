from collections import deque

# input
input = __import__('sys').stdin.readline
n, p = map(int, input().split())

def move(i, k):
    if k == 0: return i * 2
    elif k == 1: return i + 1
    else: return i - 1
    

def solve():
    global p
    visit = [0] * 100002
    q = deque()
    q.append((n))
    visit[n] = 1
    ans = 0
    while q:
        for _ in range(len(q)):
            i = q.popleft()
            if i == p: return ans
        
            for k in range(3):
                x = move(i, k)
                if not(0 <= x <= 100000): continue
                if visit[x] == 0:
                    q.append((x))
                    visit[x] = 1
        ans += 1
    return -1

print(solve())