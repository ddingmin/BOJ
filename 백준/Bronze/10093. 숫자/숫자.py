import sys

input = sys.stdin.readline

def solve(n, m):
    answer = []
    for i in range(min(n, m) + 1, max(m, n)):
        answer.append(i)
    print(len(answer))
    return sorted(answer)

n, m = map(int, input().split())
print(*solve(n, m))