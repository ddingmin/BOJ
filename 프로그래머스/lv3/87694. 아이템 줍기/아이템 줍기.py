from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def solution(rectangle, characterX, characterY, itemX, itemY):
    maps = [[0] * 101 for _ in range(101)]
    
    for line in rectangle:
        x1, y1, x2, y2 = line
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                maps[i][j] = 1
    for line in rectangle:
        x1, y1, x2, y2 = line
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                maps[i][j] = 0
    q = deque()
    q.append([characterX * 2, characterY * 2, 0])
    visit = [[0] * 101 for _ in range(101)]
    visit[characterX * 2][characterY * 2] = 1

    while q:
        for _ in range(len(q)):
            i, j, move = q.popleft()
            if (i == itemX * 2 and j == itemY * 2):
                return move // 2
            for dir in range(4):
                x, y = i + dx[dir], j + dy[dir]
                if not (0 <= x < 101 and 0 <= y < 101): continue
                if visit[x][y] == 1: continue
                if maps[x][y] == 1:
                    visit[x][y] = 1
                    q.append([x, y, move + 1])
    answer = 0
    return answer