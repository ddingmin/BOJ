from collections import deque

input = __import__('sys').stdin.readline

n = int(input())
l = int(input())

q = deque()
check = [False] * (n + 1) 
v = {}

q.append(1)
check[1] = True
ans = 0

for _ in range(l):
    a, b = map(int, input().split())
    if a in v.keys():
        v[a].append(b)
    else:
        v[a] = [b]
    if b in v.keys():
        v[b].append(a)
    else:
        v[b] = [a]
    

while(q):
    temp = q.popleft()
    for i in v[temp]:
        if check[i]:
            continue
        check[i] = True
        q.append(i)
        ans += 1

print(ans)