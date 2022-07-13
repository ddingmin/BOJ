from collections import deque
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visit = [[0] * m for _ in range(n)]
Air = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 외부공기만 1로 바꾸기
def innerAir(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y]= 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not(0 <= x < n and 0 <= y < m): continue
            if visit[x][y] == 1: continue
            if arr[x][y] == 1: continue
            visit[x][y] = 1
            Air[x][y] = 1
            q.append((x, y))

# 먼저 외부, 내부 공기 분리해놓고 시작
innerAir(0, 0)
ans = 0
while 1:
    # arr의 합이 0이면 (치즈가 모두 녹은 경우) 탈출
    check = 0
    for k in arr:
        check += sum(k)
    if check == 0: break
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                temp = 0
				# 4방향 확인해서 녹는 경우인지 체크
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]
                    if Air[x][y]: temp += 1
                if temp >= 2: # 녹은 경우 0으로 바꾸어줌
                    arr[i][j] = 0

	#bfs 재사용을 위한 visit 초기화
    visit = [[0] * m for _ in range(n)]
    innerAir(0, 0)
    ans += 1
print(ans)
