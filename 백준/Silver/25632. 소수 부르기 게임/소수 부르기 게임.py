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
def solve(a, b, c, d):
    # 소수 세팅
    prime = [1] * 1001
    for i in range(2):
        prime[i] = 0
    for i in range(2, 1001):
        if prime[i] == 0: continue
        for j in range(2, 1001):
            idx = i * j
            if idx > 1000: break
            prime[idx] = 0

    aa, bb, cc = 0, 0, 0
    for i in range(2, 1001):
        if prime[i] == 0: continue
        if a <= i <= b and c <= i <= d:
            cc += 1
        elif a <= i <= b:
            aa += 1
        elif c <= i <= d:
            bb += 1

    while 1:
        if cc: cc -= 1
        else:
            if aa: aa -= 1
            else:
                return "yj"

        if cc: cc -= 1
        else:
            if bb: bb -= 1
            else:
                return "yt"



# input
a, b = map(int, input().split())
c, d = map(int, input().split())
print(solve(a, b, c, d))


