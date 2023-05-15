import sys
import heapq

input = sys.stdin.readline


######################### solve ###############################
def solve():
    n, m, target_len = map(int, input().split())
    start, node1, node2 = map(int, input().split())

    adj = [[] for _ in range(n + 1)]
    visit = [100000000] * (n + 1)
    targets = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        # g -> h 교차로를 지나는 cost를 -0.1 해주어 동일한 cost일 때 항상 지나도록
        if (a == node1 and b == node2) or (a == node2 and b == node1):
            c -= 0.1
        adj[a].append([b, c])
        adj[b].append([a, c])

    for _ in range(target_len):
        targets.append(int(input()))

    # 다익
    hq = []
    heapq.heappush(hq, [0, start])
    visit[start] = 0
    while hq:
        cur_cost, cur_node = heapq.heappop(hq)
        if cur_cost != visit[cur_node]:
            continue
        for next_node, mcost in adj[cur_node]:
            moving_cost = cur_cost + mcost
            if visit[next_node] > moving_cost:
                visit[next_node] = moving_cost
                heapq.heappush(hq, [moving_cost, next_node])

    answer = []
    for target in targets:
        # float라면 지나야할 곳을 지난 것
        if isinstance(visit[target], float):
            answer.append(target)
    return sorted(answer)


###############################################################

t = int(input())
for _ in range(t):
    ans = solve()
    if ans:
        print(*ans)
