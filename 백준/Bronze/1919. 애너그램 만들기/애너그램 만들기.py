d = {}
a = list(input())
b = list(input())

for aa in a:
    if aa in d:
        d[aa] += 1
    else:
        d[aa] = 1

for bb in b:
    if bb in d:
        d[bb] -= 1
    else:
        d[bb] = -1

ans = 0
for i in d.keys():
    ans += abs(d[i])

print(ans)