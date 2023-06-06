import sys
input = sys.stdin.readline

# init
n = int(input())
pairs = [list(map(int, input().split())) for _ in range(n)]
pairs.append(pairs[0])

a, b = 0, 0
for i in range(n):
    a += pairs[i][0] * pairs[i + 1][1]
    b += pairs[i][1] * pairs[i + 1][0]
# a, b = abs(a), abs(b)
print(round(abs(b - a) / 2, 1))