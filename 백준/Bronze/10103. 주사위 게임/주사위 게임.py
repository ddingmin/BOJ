import sys
input = sys.stdin.readline

a, b = 100, 100

m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    if i == j: continue
    elif i > j:
        b -= i
    else:
        a -= j
print(a)
print(b)