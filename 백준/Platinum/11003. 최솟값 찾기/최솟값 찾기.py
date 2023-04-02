import sys
import heapq
from collections import deque
from bisect import bisect_left
import math
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(n, l, nums):
    q = deque()
    answer = []
    for i in range(n):
        # 인덱스 조정
        while q and q[0][0] < i - l + 1:
            q.popleft()
        # 이미 들어가 있는 수가 더 크다면 (최소값일 수가 없음)
        while q and q[-1][1] > nums[i]:
            q.pop()
        
        q.append([i, nums[i]])
        answer.append(q[0][1])
        
    return answer

# input
n, l = map(int, input().split())
nums = list(map(int, input().split()))
print(*solve(n, l, nums))
