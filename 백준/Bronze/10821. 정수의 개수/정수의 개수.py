ans = 0
for i in input().split(','):
    if i.isdecimal():
        ans += 1
print(ans)