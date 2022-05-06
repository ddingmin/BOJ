from collections import deque
input = __import__('sys').stdin.readline

n = int(input())


dq = deque()
arr = list(map(int, input().split()))

sel = 0
ans = []

for i in range(n):
    dq.append((arr[i], i+1))
while len(dq) > 0:
    t = dq.popleft()
    temp = t[0]
    ans.append(t[1])
    if not dq: break
    if temp < 0:
        for i in range(abs(temp)):
            dq.appendleft(dq.pop())

    else:
        for i in range(abs(temp) - 1):
            dq.append(dq.popleft())
    
print(" ".join(map(str,ans)))
