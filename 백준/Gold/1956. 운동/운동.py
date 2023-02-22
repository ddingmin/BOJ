import heapq
import sys
input = sys.stdin.readline



def solve(v, adj):
    def cal(start):
        hq = []
        costs = [float('inf')] * (v + 1)
        heapq.heappush(hq, [0, start])
        costs[start] = 0
        
        temp = float('inf')
        
        while hq:
            cur_cost, cur_node = heapq.heappop(hq)
            if costs[cur_node] != cur_cost: continue
            for next_node, next_cost in adj[cur_node]:
                sum_cost = cur_cost + next_cost
                if next_node == start:
                    temp = min(temp, sum_cost)
                if costs[next_node] > sum_cost:
                    costs[next_node] = sum_cost
                    heapq.heappush(hq, [sum_cost, next_node])
        return temp
    answer = float('inf')
    for i in range(1, v + 1):
        answer = min(answer, cal(i))
    if answer == float('inf'): return -1
    return answer
    
v, e = map(int, input().split())
adj = [[] for _ in range(v + 1)]
for _ in range(e):
    s, e, cost = map(int, input().split())
    adj[s].append([e, cost])

print(solve(v, adj))