from collections import deque
input = __import__('sys').stdin.readline

# input
n, k = map(int, input().split())
arr = []
# visit = [[0] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
virus = [deque() for _ in range(1001)]
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(n):
        # 입력받을 때 맵에 0이 아닌 수가 입력되면 해당 수의 바이러스 좌표를 추가
        if arr[i][j] != 0: virus[arr[i][j]].append((i, j))
second, x, y = map(int, input().split())
target = [x - 1, y - 1]

# solve
def solve():
    def bfs():
        for _ in range(second):
            for idx in range(1, 1001):
                # idx번 바이러스가 존재하지 않을 경우 넘어가기
                if not virus[idx]: continue
                for _ in range(len(virus[idx])):
                    i, j = virus[idx].popleft()
                    for dir in range(4):
                        x, y = i + dx[dir], j + dy[dir]
                        if not(0 <= x < n and 0 <= y < n): continue
                        # 방문하지 않고 해당 칸이 비어있다면
                        if arr[x][y] == 0:
                            virus[idx].append((x, y))
                            arr[x][y] = idx
        return arr[target[0]][target[1]]
    return bfs()
        
print(solve())
