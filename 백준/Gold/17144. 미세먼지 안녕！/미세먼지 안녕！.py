dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def solve(r, c, t, maps):
    # 공기 청정기 좌표 저장
    fresher = []
    for i in range(r):
        if maps[i][0] == -1: fresher.append((i, 0))
    
    def difussion():
        # 확산
        nonlocal maps
        scores = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if maps[i][j] > 0:
                    temp = maps[i][j]
                    for dir in range(4):
                        x, y = i + dx[dir], j + dy[dir]
                        if not(0 <= x < r and 0 <= y < c): continue
                        if maps[x][y] == -1: continue
                        scores[x][y] += maps[i][j] // 5
                        temp -= maps[i][j] // 5
                    scores[i][j] += temp
    
        maps = scores.copy()
        for x, y in fresher:
            maps[x][y] = -1
        return
    
    def freshing():
        nonlocal maps
        # 위쪽 공기청정기 순환
        i, j = fresher[0]
        temp = 0
        while 0 <= j + 1 < c:
            temp, maps[i][j + 1] = maps[i][j + 1], temp
            j += 1
        while 0 <= i - 1 < r:
            temp, maps[i - 1][j] = maps[i - 1][j], temp
            i -= 1
        while 0 <= j - 1 < c:
            temp, maps[i][j - 1] = maps[i][j - 1], temp
            j -= 1
        while 0 <= i + 1 < r and maps[i + 1][j] != -1:
            temp, maps[i + 1][j] = maps[i + 1][j], temp
            i += 1
        # 아래 공기청정기 순환
        i, j = fresher[1]
        temp = 0
        while 0 <= j + 1 < c:
            temp, maps[i][j + 1] = maps[i][j + 1], temp
            j += 1
        while 0 <= i + 1 < r:
            temp, maps[i + 1][j] = maps[i + 1][j], temp
            i += 1
        while 0 <= j - 1 < c:
            temp, maps[i][j - 1] = maps[i][j - 1], temp
            j -= 1
        while 0 <= i - 1 < r and maps[i - 1][j] != -1:
            temp, maps[i - 1][j] = maps[i - 1][j], temp
            i -= 1
    
    def result():
        answer = 0
        for i in range(r):
            for j in range(c):
                if maps[i][j] > 0:
                    answer += maps[i][j]
        return answer
                    
    for _ in range(t):
        difussion()
        freshing()
    return result()

r, c, t = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(r)]
print(solve(r, c, t, maps))