import sys

# input = sys.stdin.readline

# input
n = int(input())
arr = [list(input().strip()) for _ in range(n)]

##################################################

# func


##################################################

# solve
ans = 0
a, b = 0, 0

for i in range(n):
    cnt, cnnt = 0, 0
    for j in range(n):
        if arr[i][j] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            a += 1

        if arr[j][i] == '.':
            cnnt += 1
        else:
            cnnt = 0
        if cnnt == 2:
            b += 1

print(a, b)
