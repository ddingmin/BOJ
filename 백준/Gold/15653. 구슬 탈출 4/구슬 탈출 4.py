from collections import deque

n, m = map(int,input().split())
arr = []

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = []
t = 10
visit = [[[[[0] * 5 for _ in range(t)] for _ in range(t)] for _ in range(t)] for _ in range(t)]

# Input / 초기 구슬 좌표 저장
for i in range(n):
    arr.append(list(input()))
    for j in range(m):
        if arr[i][j] == 'R': rx, ry = i, j
        elif arr[i][j] == 'B': bx, by = i, j

arr[rx][ry] = '.'
arr[bx][by] = '.'




def selectBeads(rx, ry, bx, by, dir):
    # 상하좌우
    if dir == 0: # 상
        if rx > bx: return bx, by, rx, ry, 'B', 'R'
        else: return rx, ry, bx, by, 'R', 'B'
    elif dir == 1: # 하
        if rx > bx: return rx, ry, bx, by, 'R', 'B'
        else: return bx, by, rx, ry, 'B', 'R'
    elif dir == 2: # 좌
        if ry > by: return bx, by, rx, ry, 'B', 'R'
        else: return rx, ry, bx, by, 'R', 'B'
    else: # 우
        if ry > by: return rx, ry, bx, by, 'R', 'B'
        else: return bx, by, rx, ry, 'B', 'R'

def tilt(rx, ry, bx, by, dir):
    # 일단 구슬 치우고
    arr[rx][ry], arr[bx][by] = '.', '.'
    if dir == 0: # 상
        fx, fy, sx, sy, color1, color2 = selectBeads(rx, ry, bx, by, dir)

        while 1:
            x, y = fx + dx[dir], fy + dy[dir]
            if arr[x][y] == '.':
                fx, fy = x, y
            elif arr[x][y] == 'O':
                fx, fy = color1, color1  # 공이 들어간 경우
                break
            else:
                arr[fx][fy] = color1
                break

        while 1:
            x, y = sx + dx[dir], sy + dy[dir]
            if arr[x][y] == '.':
                sx, sy = x, y
            elif arr[x][y] == 'O':
                sx, sy = color2, color2  # 공이 들어간 경우
                break
            else:
                arr[sx][sy] = color2
                break

    elif dir == 1: # 하
        fx, fy, sx, sy, color1, color2 = selectBeads(rx, ry, bx, by, dir)

        while 1:
            x, y = fx + dx[dir], fy + dy[dir]
            if arr[x][y] == '.':
                fx, fy = x, y
            elif arr[x][y] == 'O':
                fx, fy = color1, color1  # 공이 들어간 경우
                break
            else:
                arr[fx][fy] = color1
                break

        while 1:
            x, y = sx + dx[dir], sy + dy[dir]
            if arr[x][y] == '.':
                sx, sy = x, y
            elif arr[x][y] == 'O':
                sx, sy = color2, color2  # 공이 들어간 경우
                break
            else:
                arr[sx][sy] = color2
                break

    elif dir == 2: # 좌
        fx, fy, sx, sy, color1, color2 = selectBeads(rx, ry, bx, by, dir)

        while 1:
            x, y = fx + dx[dir], fy + dy[dir]
            if arr[x][y] == '.':
                fx, fy = x, y
            elif arr[x][y] == 'O':
                fx, fy = color1, color1  # 공이 들어간 경우
                break
            else:
                arr[fx][fy] = color1
                break

        while 1:
            x, y = sx + dx[dir], sy + dy[dir]
            if arr[x][y] == '.':
                sx, sy = x, y
            elif arr[x][y] == 'O':
                sx, sy = color2, color2  # 공이 들어간 경우
                break
            else:
                arr[sx][sy] = color2
                break
    else: # 우
        fx, fy, sx, sy, color1, color2 = selectBeads(rx, ry, bx, by, dir)

        while 1:
            x, y = fx + dx[dir], fy + dy[dir]
            if arr[x][y] == '.':
                fx, fy = x, y
            elif arr[x][y] == 'O':
                fx, fy = color1, color1  # 공이 들어간 경우
                break
            else:
                arr[fx][fy] = color1
                break

        while 1:
            x, y = sx + dx[dir], sy + dy[dir]
            if arr[x][y] == '.':
                sx, sy = x, y
            elif arr[x][y] == 'O':
                sx, sy = color2, color2  # 공이 들어간 경우
                break
            else:
                arr[sx][sy] = color2
                break

    # for k in arr:
    #     print(*k)
    # print()
    if not(fx == 'R' or fx == 'B'): arr[fx][fy] = '.'
    if not(sx == 'R' or sx == 'B'): arr[sx][sy] = '.'
    if color1 == 'R': return fx, fy, sx, sy
    else: return sx, sy, fx, fy

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 4))
    while q:
        rrx, rry, bbx, bby, d = q.popleft()
        for dir in range(4):
            rx, ry, bx, by = tilt(rrx, rry, bbx, bby, dir)
            if bx == 'B':
                continue
            if rx == 'R':
                return visit[rrx][rry][bbx][bby][d] + 1
            # if visit[rx][ry][bx][by][dir] >= 10: return -1
            if visit[rx][ry][bx][by][dir] >= 1: continue

            q.append((rx, ry, bx, by, dir))
            visit[rx][ry][bx][by][dir] = visit[rrx][rry][bbx][bby][d] + 1
    return -1

print(bfs(rx, ry, bx, by))
