import sys
import math
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
fire_ball = deque()
maps = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, mi, s, d = map(int, input().split())
    maps[r - 1][c - 1].append([mi, s, d])


# 보기
def view():
    for m in maps:
        print(*m)
    print()


# 이동
def move():
    global maps
    moved = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if len(maps[i][j]) == 0: continue
            for kg, s, d in maps[i][j]:
                moved[(i + (dx[d] * s)) % n][(j + (dy[d] * s)) % n].append([kg, s, d])
    maps = moved


# 나누기
def div():
    global maps
    for i in range(n):
        for j in range(n):
            if len(maps[i][j]) < 2:
                continue
            new = []
            is_dir_same = True
            sum_kg, sum_s = 0, 0
            for idx in range(len(maps[i][j])):
                kg, s, d = maps[i][j][idx]
                if maps[i][j][idx - 1][2] % 2 != d % 2: is_dir_same = False
                sum_kg += kg
                sum_s += s
            next_kg = math.floor(sum_kg / 5)
            next_s = math.floor(sum_s / len(maps[i][j]))
            
            if next_kg == 0:
                new = []
            else:
                if is_dir_same: ds = [0, 2, 4, 6]
                else: ds = [1, 3, 5, 7]
                
                for d in ds:
                    new.append([next_kg, next_s, d])
            maps[i][j] = new

# 답 구하기
def find_answer():
    answer = 0
    for i in range(n):
        for j in range(n):
            for kg, s, d in maps[i][j]:
                answer += kg
    return answer


# view()
for _ in range(k):
    move()
    # print("after move")
    # view()
    div()
    # print("after div")
    # view()

print(find_answer())