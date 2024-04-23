ans = float('inf')
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    ans = min(ans, max(a, b))
print(ans)
