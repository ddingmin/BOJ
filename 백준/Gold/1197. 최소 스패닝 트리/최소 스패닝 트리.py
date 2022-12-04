# Kruskal
input = __import__('sys').stdin.readline

V, E = map(int, input().split())
edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])

# 가장 작은 가중치의 간선부터 연결하기 위해 가중치 기준 오름차순 정렬
edges.sort(key = lambda x: x[2])

# 부모를 찾는 함수
def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]

# 더 부모 합치기
def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
parent = [0] * (V + 1)
for i in range(V + 1):
    parent[i] = i

ans_cost = 0

for s, e, cost in edges:
    # 부모가 같은 경우 (사이클이 이어지는 경우) -> 간선을 이으면 안됨
    if find(parent, s) == find(parent, e): continue
    
    # 부모가 다른 경우는 간선 이어주고 가중치 ++
    union(parent, s, e)
    ans_cost += cost

print(ans_cost)
