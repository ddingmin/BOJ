from collections import deque

input = __import__('sys').stdin.readline

n, m, vum = map(int, input().split())

check = [False] * (n + 1) 
v = [[] for _ in range(1002)]

for _ in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

for i in range(1, n+1):
    v[i].sort()


ans = []
def dfs(g):
    check[g] = True
    ans.append(g)
    for i in v[g]:
        if not check[i]:
            dfs(i)

dfs(vum)
print(" ".join(map(str,ans)))

q = deque()
check = [False] * (n + 1)
q.append(vum)
check[vum] = True
ans = []


while(q):
    temp = q.popleft()
    ans.append(temp)
    for i in v[temp]:
        if check[i]:
            continue
        check[i] = True
        q.append(i)

print(" ".join(map(str,ans)))


