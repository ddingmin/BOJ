import sys
import heapq
from collections import deque
from bisect import bisect_left
import math
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
star = ['*']

def solve(n):
    for i in range(n):
        if i % 2 == 0:
            print(*(star * n))
        else:
            print(" ", end = "")
            print(*(star * n))
    return 0

# input
n = int(input())
solve(n)
