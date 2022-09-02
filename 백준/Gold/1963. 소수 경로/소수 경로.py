from collections import deque

# input
input = __import__('sys').stdin.readline

# 소수 배열 만들기.
prime = [1] * 10000
prime[0] = 0
prime[1] = 0
for i in range(2, 5001):
    for j in range(2, 5001):
        if (i * j) < 10000: prime[i * j] = 0
        else: break

def list2int(temp):
    r = 0
    for i in range(4):
        r += temp[i] * (10 ** (3 - i))
    return r

def do(a, b):
    visit = [0] * 10000
    q = deque()
    q.append((a))
    visit[a] = 1
    ans = 0

    while q:
        for _ in range(len(q)):
            temp = [0] * 4
            i = q.popleft()
            if i == b: return ans

            # 배열에 집어넣기
            temp[0] = i // 1000
            i %= 1000
            temp[1] = i // 100
            i %= 100
            temp[2] = i // 10
            i %= 10
            temp[3] = i // 1

            for k in range(4):
                for kk in range(10):
                    target = temp.copy()

                    target[k] = kk
                    
                    num = list2int(target)
                    if num < 1000: continue
                    if visit[num] == 0 and prime[num] == 1:
                        visit[num] = 1
                        q.append((num))
        ans += 1
    return "Impossible"

def solve():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(do(a, b))

solve()