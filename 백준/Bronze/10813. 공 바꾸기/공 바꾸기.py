import sys
input = sys.stdin.readline

n, m = map(int, input().split())
balls = []
for i in range(n):
    balls.append(i + 1)
for _ in range(m):
    a, b = map(int, input().split())
    balls[a - 1], balls[b - 1] = balls[b - 1], balls[a - 1]
print(*balls)