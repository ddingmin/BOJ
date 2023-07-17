import sys
input = sys.stdin.readline

ans = 0

while 1:
    n = int(input())

    if n == -1:
        break
    ans += n

print(ans)