n, k = map(int, input().split())

cnt = 0
binN = bin(n)

while binN.count('1') > k:
    n += 1
    cnt += 1
    binN = bin(n)

print(cnt)