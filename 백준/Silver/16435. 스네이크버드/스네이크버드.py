n, m = map(int,input().split())
arr = sorted(list(map(int,input().split())))

for i in arr:
    if m >= i:
        m += 1
    else:
        break
print(m)
