import sys
import math
from itertools import combinations as cb
from itertools import permutations as pm
from collections import deque

# sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
MOD = 10_007
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


# solve


# input
n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = arr[-1] - arr[0]
low = arr[0]
for i in range(1, m + 1):
    low = min(low, arr[i])
    ans = max(ans, arr[n + i - m - 1] - low)

print(ans)

