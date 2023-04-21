import sys
input = sys.stdin.readline

n, m = map(int, input().split())
balls = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    i -= 1
    j -= 1
    for idx in range(i, j + 1):
        balls[idx] = k
print(*balls)