c = input()
ans = 0
for i in c:
    i = int(i)
    if i == 0: ans += 9
    else: ans += i
print(ans)