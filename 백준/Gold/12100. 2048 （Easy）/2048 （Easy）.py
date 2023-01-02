n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

def turn(current_arr):
    size = len(current_arr)
    temp_arr = [[0] * size for _ in range(size)]
    for r in range(size):
        for c in range(size):
            temp_arr[c][size - 1 - r] = current_arr[r][c]
    return temp_arr

def move(current_arr, direction):
    max_block = 0
    
    # print("current")
    # for k in current_arr:
    #     print(*k)
    # print()
    
    for _ in range(direction):
        current_arr = turn(current_arr)    
    
    next_arr = [[0] * n for _ in range(n)]
    
    for i in range(n):
        setting = 0
        new_step = []
        for j in range(n):
            if setting == 0:
                setting = current_arr[i][j]
            elif setting != 0 and current_arr[i][j] != 0:
                if setting == current_arr[i][j]:
                    # 합치기
                    new_step.append(setting * 2)
                    setting = 0
                else:
                    # 안합치기
                    new_step.append(setting)
                    setting = current_arr[i][j]
        # 마지막 한번 더
        new_step.append(setting)
        
        # 갱신
        for j in range(n):
            if j < len(new_step):
                next_arr[i][j] = new_step[j]
            else:
                next_arr[i][j] = 0
        max_block = max(max_block, max(next_arr[i]))

    # 원상 복구
    for i in range(4 - direction):
        next_arr = turn(next_arr)
    
    # print("next")
    # for k in next_arr:
    #     print(*k)
    # print()
    # print(max_block)
    
    return next_arr, max_block

answer = 0

def backtrack(arr, depth):    
    global answer
    if depth == 5:
        return

    for dir in range(4):
        new_arr, new_block = move(arr, dir)
        answer = max(answer, new_block)
        if new_arr == arr:
            continue
        backtrack(new_arr, depth + 1)
        

backtrack(arr, 0)
print(answer)