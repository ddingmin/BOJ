import sys
from collections import deque

MAX_NODE = 60


def to_int(node, index_dic):
    if node not in index_dic:
        index_dic[node] = len(index_dic) + 1
    return index_dic[node]


def solve(capacity, flow, adj, start, end):
    ans = 0

    while 1:
        visit = [0] * MAX_NODE
        q = deque([start])

        while q and visit[end] == 0:  # 큐가 존재하고 마지막 노드에 도달하지 않았다면
            cur = q.popleft()
            for nxt in adj[cur]:
                if not visit[nxt] and capacity[cur][nxt] - flow[cur][nxt] > 0:  # 방문하지 않고 흐를 공간이 존재하면
                    q.append(nxt)
                    visit[nxt] = cur

                    if nxt == end:  # 마지막 노드에 도달하면 멈추기
                        break
        # BFS를 돌려 더이상 마지막 노드에 흐르지 못한 경우 중지
        if visit[end] == 0:
            break

        # 가장 낮은 구간의 흐를 수 있는 양 찾기
        min_flow = float('inf')

        node = end
        while node != start:
            min_flow = min(min_flow, capacity[visit[node]][node] - flow[visit[node]][node])
            node = visit[node]

        # 흐를 수 있는 양 흐르게
        node = end
        while node != start:
            flow[visit[node]][node] += min_flow  # 흐르게
            flow[node][visit[node]] -= min_flow  # 역방향도 갱신
            node = visit[node]

        # 총 흐르는 양 갱신
        ans += min_flow
    return ans


def main():
    n = int(input())
    adj = [[] for _ in range(MAX_NODE)]
    capacity = [[0] * MAX_NODE for _ in range(MAX_NODE)]
    flow = [[0] * MAX_NODE for _ in range(MAX_NODE)]
    index_dic = {}

    for _ in range(n):
        a, b, c = input().split()
        a, b, c = to_int(a, index_dic), to_int(b, index_dic), int(c)
        capacity[a][b] += c
        capacity[b][a] += c
        adj[a].append(b)
        adj[b].append(a)

    start, end = index_dic['A'], index_dic['Z']
    print(solve(capacity, flow, adj, start, end))


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 5)
    input = sys.stdin.readline
    main()
