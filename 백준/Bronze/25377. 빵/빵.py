ans = float('inf')
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    if a > b: continue
    ans = min(ans, max(a, b))

if ans == float('inf'):
    print(-1)
else:
    print(ans)