n = int(input())
a, b, c = map(int, input().split())

ans = 0

ans += min(a, n)
ans += min(b, n)
ans += min(c, n)

print(ans)