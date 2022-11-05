n, m = map(int, input().split())
m = max(m, n - m)
ans = 1

for i in range(n - m):
    ans *= (n - i)

for i in range(1, n - m + 1):
    ans //= i
    
print(ans)