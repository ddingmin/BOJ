n = int(input())
adj = [[] for _ in range(n + 1)]

for i in range(n):
    temp = int(input())
    adj[temp].append(i + 1)

cycle = [0] * (n + 1)

def dfs(start_node, current_node, visit):
    for next_node in adj[current_node]:
        if not visit[next_node]:
            # 사이클이 된 경우
            visit[next_node] = 1
            if next_node == start_node:
                for i in range(1, n + 1):
                    if visit[i]: cycle[i] = 1
                visit[next_node] = 0
                return
            dfs(start_node, next_node, visit)
            visit[next_node] = 0

def check():
    visit = [0] * (n + 1)
    for node in range(1, n + 1):
        dfs(node, node, visit)
    return
    
    
# 모든 노드를 돌면서 사이클 확인
check()
print(sum(cycle))
for i in range(1, n + 1):
    if cycle[i]: print(i)
