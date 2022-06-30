n, m, x, y, k = map(int, input().split())

arr = []

dice = [0, 0, 0, 0, 0, 0] # 위 동 서 남 북 아래

for _ in range(n):
    arr.append(list(map(int, input().split())))
do = list(map(int, input().split()))

def turn(i):
    over, right, left, down, up, under = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if i == 1: # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = left, over, under, down, up, right
    elif i == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = right, under, over, down, up, left
    elif i == 3: # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = down, right, left, under, over, up
    elif i == 4: # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = up, right, left, over, under, down

def punch(i, j):
    if arr[i][j] == 0: 
        arr[i][j] = dice[5]
    else:
        dice[5] = arr[i][j]
        arr[i][j] = 0
    print(dice[0])


for doing in range(k):
    if do[doing] == 1: # 동쪽
        if 0 <= y + 1 < m:
            y += 1
            turn(1)
            punch(x, y)
    elif do[doing] == 4: # 남쪽
        if 0 <= x + 1 < n:
            x += 1
            turn(4)
            punch(x, y)
    elif do[doing] == 3: # 북쪽
        if 0 <= x - 1 < n:
            x -= 1
            turn(3)
            punch(x, y)
    elif do[doing] == 2: # 서쪽
        if 0 <= y - 1 < m:
            y -= 1
            turn(2)
            punch(x, y)