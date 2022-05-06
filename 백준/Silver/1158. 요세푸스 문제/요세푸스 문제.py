from collections import deque
input = __import__('sys').stdin.readline

n, temp = map(int,input().split())
dq = deque()

arr = list(map(int, input().split()))

ans = []

for i in range(n):
    dq.append(i+1)

while len(dq) > 0:
    for i in range(abs(temp) - 1):
        dq.append(dq.popleft())
    ans.append(dq.popleft())
    if not dq: break

print("<" + ", ".join(map(str,ans)), end=">")