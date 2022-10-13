input = __import__('sys').stdin.readline

n = int(input())
d = {}
id = []
for _ in range(n):
    a, b = input().strip().split('.')
    if b in d:
        d[b] += 1
    else:
        d[b] = 1
        id.append(b)

id.sort()
for name in id:
    print(name, d[name])
