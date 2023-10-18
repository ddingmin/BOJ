import sys
from collections import deque

input = sys.stdin.readline

# input
while 1:
    n, m = map(int, input().split())
    if (n, m) == (0, 0): break
    has = {}

    cnt = 0

    for _ in range(n):
        has[int(input())] = 1

    for _ in range(m):
        if int(input()) in has:
            cnt += 1

    print(cnt)
