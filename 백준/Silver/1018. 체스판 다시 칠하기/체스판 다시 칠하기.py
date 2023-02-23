import sys
input = sys.stdin.readline

def calc(x, y, maps):
    count = [0, 0]
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if maps[x + i][y + j] == 'W': count[0] += 1
                elif maps[x + i][y + j] == 'B': count[1] += 1
            else:
                if maps[x + i][y + j] == 'B': count[0] += 1
                elif maps[x + i][y + j] == 'W': count[1] += 1
    return min(count)

def solve(n, m, maps):
    answer = float('inf')
    
    for x in range(n - 7):
        for y in range(m - 7):
            answer = min(answer, calc(x, y, maps))
    return answer

n, m = map(int, input().split())
maps = [list(input().strip()) for _ in range(n)]
print(solve(n, m, maps))