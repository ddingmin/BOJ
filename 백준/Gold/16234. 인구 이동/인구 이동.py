from collections import deque
input = __import__('sys').stdin.readline

n, l, r = map(int, input().split())
arr = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(n):
    arr.append(list(map(int, input().split())))

def bfs(x, y):
    # 기본 세팅
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    _sum = arr[x][y]    # 인구 이동이 발생 시 나누어주기 위한 값
    near = [(x, y)]     # 인구 이동 발생될 나라들
    while q:
        i, j = q.popleft()
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if not(0 <= x < n and 0 <= y < n): continue
            if visit[x][y] == 1: continue
            if l <= abs(arr[i][j] - arr[x][y]) <= r:    # 인구 이동 가능한 나라
                _sum += arr[x][y]   # 해당 나라의 인구를 더해주고
                visit[x][y] = 1
                q.append((x, y))
                near.append((x, y)) # 해당 나라를 추가
    
    change = _sum // len(near)  # 인구 이동 완료 후 값
    flag = False    # 값이 변경되었는지 저장하는 배열
    for x, y in near:
        if arr[x][y] != change: 
            flag = True # 변경된 값이 존재하면 True
        
    return flag, change, near

cnt = 0
while 1:
    flag = False
    visit = [[0] * n for _ in range(n)]
    temp = []   # 변경할 값 잠시 저장할 리스트
    for i in range(n):
        for j in range(n):
            f, c, near = bfs(i, j)
            if f: # 변경할 값이 존재한다면
                for x, y in near:   # temp에 변경할 값 추가
                    temp.append((x, y, c))  # 좌표, 변경할 값
                flag = True   # 값이 한번이라도 변경되면 True
    if not flag: break  # 값이 한번도 변경되지 않았으면 멈추기
    
    # 인구 이동 후 변경된 값 갱신
    for x, y, c in temp:
        arr[x][y] = c
    cnt += 1

print(cnt)