import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

t = int(input())
for _ in range(t):
    n = int(input())
    parent = {}
    parent_count = {}
    
    def find_parent(a):
        if a != parent[a]:
            parent[a] = find_parent(parent[a])
        return parent[a]
    
    def union(a, b):
        a, b = find_parent(a), find_parent(b)
        # a, b가 친구 관계가 아니라면 합치기
        if a != b:
            parent[b] = a
            parent_count[a] += parent_count[b]
        return parent_count[a]
    
    for _ in range(n):
        a, b = input().split()
        if not a in parent:
            parent[a] = a
            parent_count[a] = 1
        if not b in parent:
            parent[b] = b
            parent_count[b] = 1

        print(union(a, b))