import sys
import heapq
from collections import deque
from bisect import bisect_left
import math
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(n, nums, x):
    s, e = 0, n - 1
    count = 0
    while s < e:
        temp = nums[s] + nums[e]
        if temp == x:
            count += 1
            e -= 1
        elif temp > x:
            e -= 1
        else:
            s += 1
    return count

# input
n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
print(solve(n, nums, x))
