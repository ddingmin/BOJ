n, m  = map(int, input().split())

arr = [list(input().strip()) for _ in range(n)]

ans = [[-1] * m for _ in range(n)]

def move():
    for i in range(n):
        for j in range(m - 1, -1, -1):
            arr[i][j] = arr[i][j - 1]

    for i in range(n):
        arr[i][0] = '.'

def check(level):
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'c' and ans[i][j] == -1:
                ans[i][j] = level

for level in range(m):
    check(level)
    move()

for pp in ans:
    print(*pp)