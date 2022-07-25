n = 1000 - int(input())
ans = 0
arr = [500, 100, 50, 10, 5, 1]
for k in arr:
    if n == 0: break
    ans += n // k
    n %= k
print(ans)