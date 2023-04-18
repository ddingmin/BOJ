import sys
import heapq
import math
from collections import deque
from bisect import bisect_left
input = sys.stdin.readline
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
# 첫 양분은 5
# 봄: 나무가 자신의 나이 만큼 양분을 섭취 (나이가 어린 나무부터 섭취)
# 양분이 부족하면 나무 사망
# 여름: 죽은 나무는 양분으로 변함 (나이 // 2)
# 가을: (5의 배수) 나무가 번식 8방향
# 겨울: 양분 추가 (주어진 양 만큼)
# 살아있는 나무의 개수 구하기
 
n, m, k = map(int, input().split())
maps = [[5] * n for _ in range(n)]
foods = [list(map(int, input().split())) for _ in range(n)]
 
trees = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, age = map(int, input().split())
    x, y = x - 1, y - 1
    trees[x][y].append(age)
 
# 나이순으로 정렬시켜서 저장
for i in range(n):
    for j in range(n):
        trees[i][j] = deque(sorted(trees[i][j]))
 
def view_tree():
    for i in range(n):
        print(trees[i], maps[i])
    print()

# 양분 섭취
def eat_food(i, j, old):
    new = deque()
    food = 0
    for _ in range(len(old)):
        # 양분 섭취 가능
        if maps[i][j] >= old[0]:
            maps[i][j] -= old[0]
            new.append(old.popleft() + 1)
        # 사망
        else:
            food += old.popleft() // 2
    trees[i][j] = new
    return food

# 번식
def breed_tree(i, j, tree):
    for t in tree:
        if t % 5 == 0:
            for k in range(8):
                x, y = i + dx[k], j + dy[k]
                if not(0 <= x < n and 0 <= y < n): continue
                breeding[x][y] += 1

def robot_give_food():
    for i in range(n):
        for j in range(n):
            maps[i][j] += foods[i][j]

def find_answer():
    count = 0
    for i in range(n):
        for j in range(n):
            count += len(trees[i][j])
    print(count)

for _ in range(k):
    # view_tree()
    die = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            die[i][j] += eat_food(i, j, trees[i][j])
    
    for i in range(n):
        for j in range(n):
            maps[i][j] += die[i][j]
    breeding = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            breed_tree(i, j, trees[i][j])
    for i in range(n):
        for j in range(n):
            for _ in range(breeding[i][j]):
                trees[i][j].appendleft(1)
    robot_give_food()

find_answer()