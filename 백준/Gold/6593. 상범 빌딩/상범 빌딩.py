from collections import deque

# input
input = __import__('sys').stdin.readline
dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]

def solve(arr, start, end, l, r, c):
    # BFS 세팅
    q = deque()
    visit = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(l)]
    k, i, j = start
    q.append((k, i, j))
    visit[k][i][j] = 1
    ans = 0
    
    while q:
        for _ in range(len(q)):
            k, i ,j = q.popleft()
            if (k, i, j) == end: return ans
            
            for dir in range(6):
                z, x, y = k + dz[dir], i + dx[dir], j + dy[dir]
                if not(0 <= z < l and 0 <= x < r and 0 <= y < c): continue
                if visit[z][x][y] == 0 and arr[z][x][y] == '.':
                    visit[z][x][y] = 1
                    q.append((z, x, y))
        ans += 1
    return -1

# main
while 1:
    # Input
    l, r, c = map(int, input().split())
    if l == r == c == 0: exit(0)    # 종료 조건
    
    arr = []
    for z in range(l):
        temp = []
        for x in range(r):
            temp.append(list(input().strip()))
        arr.append(temp)
        input() # 한 층을 입력 받고 1line 입력 받기

        # 시작 위치, 탈출 위치 좌표 설정
        for x in range(r):
            for y in range(c):
                if arr[z][x][y] == 'S': 
                    start = (z, x, y)
                    arr[z][x][y] = '.'
                
                if arr[z][x][y] == 'E': 
                    end = (z, x, y)
                    arr[z][x][y] = '.'
    
    ans = solve(arr, start, end, l, r, c)
    
    # Output
    if ans >= 0: print("Escaped in" , str(ans) , "minute(s).")
    else: print("Trapped!")
    