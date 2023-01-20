t = int(input())


apart = [[0] * (15) for _ in range(15)]
for i in range(1, 15):
    apart[0][i] = i

for i in range(1, 15):
    sumfix = 0
    for j in range(1, 15):
        sumfix += apart[i - 1][j]
        apart[i][j] = sumfix
for _ in range(t):
    k = int(input()) # 층
    n = int(input()) # 호
    print(apart[k][n])
    