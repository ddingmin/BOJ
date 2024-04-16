n = int(input())
price = int(input())

ans = [price]

if n >= 5:
    ans.append(price - 500)
if n >= 10:
    ans.append(price - price * 0.1)
if n >= 15:
    ans.append(price - 2000)
if n >= 20:
    ans.append(price - price * 0.25)

print(max(0, int(min(ans))))
