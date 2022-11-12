a, b  = map(int, input().split())
ans = ((a + b) // 2, a - (a + b) // 2)
ans = (max(ans), min(ans))

if (sum(ans) == a and (max(ans) - min(ans) == b)) and ans[0] >= 0 and ans[1] >= 0:
    print(*ans)
else:
    print(-1)

