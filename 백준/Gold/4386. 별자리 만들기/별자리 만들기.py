# Kruskal
input = __import__('sys').stdin.readline

def calculate_cost(a, b):
    a, b = abs(a[0] - b[0]), abs(a[1] - b[1])
    return (a ** 2 + b ** 2) ** (1 / 2)

n = int(input())
V = 100

xy = []
for i in range(n):
    x, y = map(float, input().split())
    xy.append((x, y))

edges = []
for i in range(n):
    start = xy[i]
    for j in range(i + 1, n):
        end = xy[j]
        cost = calculate_cost(start, end)
        edges.append([i, j, cost])

# 가장 작은 가중치의 간선부터 연결하기 위해 가중치 기준 오름차순 정렬
edges.sort(key = lambda x: x[2])

# 부모를 찾는 함수
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
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

cnt = 0
for s, e, cost in edges:
    if cnt == V - 1: break
    # 부모가 같은 경우 (사이클이 이어지는 경우) -> 간선을 이으면 안됨
    if find(parent, s) == find(parent, e): continue
    
    # 부모가 다른 경우는 간선 이어주고 가중치 ++
    union(parent, s, e)
    ans_cost += cost
    cnt += 1

print(ans_cost)
