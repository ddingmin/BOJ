n = str(input())

d = {}

for i in n:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for k in d.keys():
    d[k] //= 2

ans = ""

if '0' in d:
    ans += '0' * d['0']

if '1' in d:
    ans += '1' * d['1']

print(ans)