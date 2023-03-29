import sys
import heapq
from collections import deque
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(n, m , nums):
    hq = []
    score = 0
    count = 0
    for i in nums:
        if score + i >= m:
            count += 1
            if hq and hq[0] < -1 * i:
                score -= (heapq.heappop(hq) * -2)
                score += i
                heapq.heappush(hq, -i)
            else:
                score -= i
        else:
            score += i
            heapq.heappush(hq, -i)

    return count

# input
n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(solve(n, m, nums))