import sys
import heapq
import math
from collections import deque
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

nums.sort()
answer = 0
start, end = nums[0]
for i in range(1, n):
    a, b = nums[i]
    if end >= a:
        end = max(b, end)
    else:
        #print(start, end)
        answer += (end - start)
        start, end = a, b
        #print()
answer += (end - start)
print(answer)