from collections import deque
N, M = map(int, input().split())

indegree = [0] * (N + 1)
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    indegree[b] += 1

q = deque()

# 차수가 0인 값 먼저 넣어주고
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

# 0인 값을 차례로 빼주면서 
while q:
    out_node = q.popleft()
    print(out_node, end = ' ')
    # 지운 노드로 부터 도착되는 노드 차수 -1
    for next in adj[out_node]:
        indegree[next] -= 1
        # 뺸 노드의 차수가 0이 되면 큐에 추가
        if indegree[next] == 0:
            q.append(next)