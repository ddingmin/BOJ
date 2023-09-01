n = list(map(int, input().split()))
n = sorted(n, reverse= 1)

ans = 0
for i in n:
    if i > 0:
        ans += 1
    else:
        break
print(ans)