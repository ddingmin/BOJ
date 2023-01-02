R, C, shark_numbers = map(int, input().split())
shark = []
for _ in range(shark_numbers):
    a, b, c, d, e = map(int, input().split())
    # 생존 여부, 좌표, 속력, 이동 방향, 크기
    shark.append([True, [a - 1, b - 1], c, d, e])

def move(user):
    return user + 1

def get_shark(user):
    selected = None
    
    for i in range(len(shark)):
        alive, xy, speed, direction, size = shark[i]
        if not alive: continue
        x, y = xy
        if y != user: continue
        
        if not selected:
            selected = [x, y, size, i]
        else:
            if x < selected[0]:
                selected = [x, y, size, i]

    if selected:
        x, y, size, i = selected
        shark[i][0] = False
        return size
    else:
        return 0

def move_one_shark(x, y, speed, direction):
    if direction == 1 or direction == 2:
        for _ in range(speed):
            if direction == 1:
                x -= 1
            else:
                x += 1
            if x == -1:
                x = 1
                direction = 2
            if x == R:
                x = R - 2
                direction = 1
        return x, y, direction

    if direction == 3 or direction == 4:
        for _ in range(speed):
            if direction == 4:
                y -= 1
            else:
                y += 1
            if y == -1:
                y = 1
                direction = 3
            if y == C:
                y = C - 2
                direction = 4
        return x, y, direction
    

def move_shark():
    map_shark_same = [[[] for _ in range(C)] for _ in range(R)]

    # 모든 상어 이동
    for i in range(len(shark)):
        alive, xy, speed, direction, size = shark[i]
        if not alive: continue
        x, y = xy
        x, y, direction = move_one_shark(x, y, speed, direction)
        map_shark_same[x][y].append((i, size))
        shark[i] = [alive, [x, y], speed, direction, size]
        
    # 같은 위치 상어 갱신
    for i in range(R):
        for j in range(C):
            if len(map_shark_same[i][j]) > 1:
                # 상어 크기순으로 정렬
                sorted_shark = sorted(map_shark_same[i][j], key= lambda sh: -sh[1])
                # 가장 큰 상어 제외 상어 죽이기
                for num in range(1, len(sorted_shark)):
                    shark[sorted_shark[num][0]][0] = False

def game(user):
    answer = 0
    for _ in range(C):
        # 낚시꾼 이동
        user = move(user)
        # 상어 사냥
        answer += get_shark(user)
        # 상어 이동
        move_shark()
    return answer

print(game(-1))
    
    