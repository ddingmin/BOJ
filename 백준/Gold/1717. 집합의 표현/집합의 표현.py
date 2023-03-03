import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
n, m = map(int, input().split())

parent = []
# 부모노드, 노드
for i in range(n + 1):
    parent.append(i)

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a, b = find_parent(a), find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    elif a == 1:
        if find_parent(b) == find_parent(c):
            print("YES")
        else:
            print("NO")
