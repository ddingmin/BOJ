n ,m = map(int, input().split())
setPrice = []
onePrice = []
for i in range(m):
    a, b = map(int, input().split())
    setPrice.append(a)
    onePrice.append(b)
setPrice.sort()
onePrice.sort()
cnt = n // 6
cntone = n % 6
temp = setPrice[0] * cnt + onePrice[0] * cntone
ans = min(temp, onePrice[0] * n)
ans = min(ans, (cnt + 1) * setPrice[0])
print(ans)