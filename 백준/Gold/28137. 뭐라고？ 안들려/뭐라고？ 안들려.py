import sys
input = sys.stdin.readline

n, k = map(int, input().split())

d = {}
for _ in range(n):
    a, b = map(int, input().split())
    temp = b - k * a
    if temp not in d:
        d[temp] = 1
    else:
        d[temp] += 1

answer = 0
for key in d:
    answer += d[key] * (d[key] - 1)
print(answer)
    