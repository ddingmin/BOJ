input = __import__('sys').stdin.readline

n = int(input())
m = int(input())

dist = [[float('inf')] * (101) for _ in range(101)]

for _ in range(m):
    a, b, c = map(int, input().split())
    # 직접 연결된 노드 최소값으로 세팅
    dist[a][b] = min(c, dist[a][b])

# 플로이드 워셜
def fw(dist, n):
    for k in range(1, n):
        # 자신 -> 자신의 거리는 0
        dist[k][k] = 0
        for i in range(1, n):
            for j in range(1, n):
                # [i -> j] 와 [i -> k] + [k -> j] 중 최소값으로 갱신
                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
    return dist

dist = fw(dist,n + 1)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == float('inf'): dist[i][j] = 0
    print(*dist[i][1:n + 1])
    