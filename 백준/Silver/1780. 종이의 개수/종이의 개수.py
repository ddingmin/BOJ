dx,dy = [0, 0, -1, 1], [-1, 1, 0, 0]
size = int(input())
arr = []
for _ in range(size):
    arr.append(list(map(int, input().split())))

def is_paint(x, y, size):
    color = arr[x][y]
    for i in range(size):
        for j in range(size):
            if arr[x + i][y + j] != color:
                return -2
    return color

def do(x, y, size):
    flag = is_paint(x, y, size)
    if flag > -2:
        answer[flag] += 1
        return
    if size == 1: return
    do(x, y, size // 3)
    do(x, y + size // 3, size // 3)
    do(x, y + 2 * (size // 3), size // 3)

    do(x + size // 3, y, size // 3)
    do(x + size // 3, y + size // 3, size // 3)
    do(x + size // 3, y + 2 * (size // 3), size // 3)

    do(x + 2 * (size // 3), y, size // 3)
    do(x + 2 * (size // 3), y + size // 3, size // 3)
    do(x + 2 * (size // 3), y + 2 * (size // 3), size // 3)

answer = [0, 0, 0]
do(0, 0, size)
print(answer[-1])
print(answer[0])
print(answer[1])