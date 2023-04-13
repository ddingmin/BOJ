import sys
import heapq
from collections import deque
from bisect import bisect_left
import math
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# input
n, k = map(int, input().split())
nums = []
terms = []
for _ in range(n):
    nums.append(int(input()))
    if len(nums) >= 2:
        terms.append(nums[-1] - nums[-2] - 1)

terms.sort(reverse= 1)
if n == 1:
    print(1)
else:
    score = nums[-1] - nums[0] + 1
    for i in range(k - 1):
        score -= terms[i]
    print(score)