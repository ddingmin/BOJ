k, n, m = map(int, input().split())
ans = max(k * n - m, 0)
print(ans)