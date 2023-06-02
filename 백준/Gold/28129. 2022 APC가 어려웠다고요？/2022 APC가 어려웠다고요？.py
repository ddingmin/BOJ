import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7
N = 3001
n, k = map(int, input().split())
pdp = [[0] * (N) for _ in range(n)]

ranges = []
for i in range(1, n + 1):
    s, e = map(int, input().split())
    ranges.append([s, e])

for i in range(ranges[0][0], ranges[0][1] + 1):
    if i > 0:
        pdp[0][i] = pdp[0][i - 1] + 1
    else:
        pdp[0][i] = 1
last_s = ranges[0][0]
last_e = ranges[0][1]

for i in range(1, n):
    for j in range(ranges[i][0], ranges[i][1] + 1):
        _min = max(j - k - 1, 0, last_s - 1)
        _max = min(j + k, N, last_e)
        pdp[i][j] = (pdp[i - 1][_max] - pdp[i - 1][_min]) % MOD
        pdp[i][j] = (pdp[i][j] + pdp[i][j - 1]) % MOD
    
    last_s = ranges[i][0]
    last_e = ranges[i][1]

print(pdp[-1][last_e])
    