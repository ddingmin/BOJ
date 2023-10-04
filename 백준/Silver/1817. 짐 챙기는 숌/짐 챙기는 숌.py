import sys
import math
from itertools import combinations as cb
from itertools import permutations as pm
from collections import deque


sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dx, dy = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, -2, -1, 1, 2]

# input
n, m = map(int, input().split())
arr = list(map(int, input().split()))
if n == 0:
    print(0)
    exit(0)
has = 0
ans = 1
for i in arr:
    if has + i > m:
        ans += 1
        has = i
    else:
        has += i
print(ans)
