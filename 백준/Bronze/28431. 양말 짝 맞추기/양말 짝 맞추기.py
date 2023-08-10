d = {}

for _ in range(5):
    n = int(input())
    if n in d:
        d[n] += 1
    else:
        d[n] = 1

for k in d.keys():
    if d[k] % 2 == 1:
        print(k)