n, m = map(int, input().split())
a = set(list(map(int, input().split())))
b = list(map(int, input().split()))
for i in range(m):
    a.discard(b[i])
print(len(a))
print(*sorted(a))