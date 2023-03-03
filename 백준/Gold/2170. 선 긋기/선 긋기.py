import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    lines.append(list(map(int, input().split())))
lines.sort()

start, end = lines[0]
answer = 0

for i in range(1, n):
    if end >= lines[i][0]:
        end = max(lines[i][1], end)
    else:
        answer += end - start
        start, end = lines[i]
answer += end - start
print(answer)
