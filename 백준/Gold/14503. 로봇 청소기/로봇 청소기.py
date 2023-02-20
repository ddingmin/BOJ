import sys
input = sys.stdin.readline

# 북동남서
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def solve(n, m, r, c, d, maps):
    answer = 0
    cleaned = [[0] * m for _ in range(n)]
    
    def cleaning(x, y):
        nonlocal answer
        nonlocal cleaned
        cleaned[x][y] = 1
        answer += 1
        return
    
    def check(i, j):
        for dir in range(4):
            x, y = i + dx[dir], j + dy[dir]
            if not(0 <= x < n and 0 <= y < m): continue
            elif maps[x][y] == 0 and cleaned[x][y] == 0:
                return True
        return False
    
    def go_back(x, y, d):
        # 후진할 수 없다면 False, 가능하면 좌표 반환
        d = (d + 2) % 4
        x, y = x + dx[d], y + dy[d]
        if not(0 <= x < n and 0 <= y < m) or maps[x][y] == 1: 
            return False
        else:
            return (x, y)

    def turn_go(i, j, d):
        d = (d + 3) % 4
        x, y = i + dx[d], j + dy[d]
        if (0 <= x < n and 0 <= y < m) and maps[x][y] == 0 and cleaned[x][y] == 0:
            return x, y, d
        else:
            return i, j, d
    
    doing = True
    while doing:
        if cleaned[r][c] == 0: cleaning(r, c)
        elif not check(r, c):
            result = go_back(r, c, d)
            if result == False: break
            r, c = result
        else:
            r, c, d = turn_go(r, c, d)
        
    return answer

n, m = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, m, r, c, d, maps))