import sys
import math
from itertools import combinations as cb
from itertools import permutations as pm
from collections import deque

# sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
MOD = 10_007
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


# solve

# input
n, m = map(int, input().split())
arr = []
for _ in range(m):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    arr.append([a, b, c])

arr.sort(key = lambda x: [x[1], x[0]])

for i in range(m):
    print(arr[i][2], end = "")
