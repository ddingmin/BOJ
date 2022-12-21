import heapq
input = __import__('sys').stdin.readline

n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    # 도착지, cost
    adj[a].append([b, c])

start, end = map(int, input().split())

hq = []
cost = [float('inf')] * (n + 1)
root = [0] * (n + 1)
cost[start] = 0
heapq.heappush(hq, [0, start])

while hq:
    current_cost, current_node = heapq.heappop(hq)
    if cost[current_node] != current_cost: continue
    for next_node, next_cost in adj[current_node]:
        if cost[next_node] > current_cost + next_cost:
            cost[next_node] = current_cost + next_cost
            root[next_node] = current_node
            heapq.heappush(hq, [cost[next_node], next_node])

city = []
back = end
while 1:
    city.append(back)
    back = root[back]
    if back == 0: break


print(cost[end])
print(len(city))
print(*city[::-1])
