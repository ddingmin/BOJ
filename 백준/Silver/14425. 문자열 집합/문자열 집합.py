import sys
input = sys.stdin.readline

n, m = map(int, input().split())
check = {}
for _ in range(n):
    check[input().strip()] = 0

for _ in range(m):
    word = input().strip()
    if word in check:
        check[word] += 1

ans = 0
for k in check:
    ans += check[k]
    
print(ans)