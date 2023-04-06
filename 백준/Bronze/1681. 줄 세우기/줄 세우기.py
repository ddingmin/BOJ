import sys
import heapq
from collections import deque
from bisect import bisect_left
import math
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(n, l):
    a = 0
    b = 0
    while b < n:
        a += 1
        if not l in str(a):
            b += 1
    return a

# input
n, l = map(int, input().split())
print(solve(n, str(l)))
