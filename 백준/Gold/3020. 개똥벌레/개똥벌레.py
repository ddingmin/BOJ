import sys
import heapq
import math
from collections import deque
from bisect import bisect_left
input = sys.stdin.readline

def solve(n, h, top, bottom):
    psum = [0]
    for i in top[::-1]:
        psum.append(psum[-1] + i)
    psum = psum[1:h + 1]

    psum2 = [0]
    for i in bottom[::-1]:
        psum2.append(psum2[-1] + i)
    psum2 = psum2[1:h + 1][::-1]

    answer = [float('inf'), 0]
    for i in range(h):
        psum[i] += psum2[i]
        if psum[i] < answer[0]:
            answer = [psum[i], 1]
        elif psum[i] == answer[0]:
            answer[1] += 1

    return answer

n, h = map(int, input().split())
top, bottom = [0] * (h + 1), [0] * (h + 1)

for _ in range(n // 2):
    bottom[int(input())] += 1
    top[int(input())] += 1

print(*solve(n, h, top, bottom))