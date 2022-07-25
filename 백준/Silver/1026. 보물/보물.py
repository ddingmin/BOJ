n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = sorted(a)
b = sorted(b, reverse= True)
ans = 0
for k in range(n):
    ans += a[k] * b[k]
print(ans)