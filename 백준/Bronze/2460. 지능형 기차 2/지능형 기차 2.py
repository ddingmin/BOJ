import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

temp = 0
ans = 0
for _ in range(10):
    a, b = map(int, input().split())
    temp -= a
    temp += b
    ans = max(temp, ans)

print(ans)