import sys
import heapq
from collections import deque
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solve(n, m , nums):
    maps = [[0] * (m) for _ in range(n)]

    for i in range(m):
        height = nums[i]
        for j in range(1, height + 1):
            maps[-j][i] = 1
    
    # for mm in maps:
    #     print(mm)

    count = 0
    for i in range(n - 1, -1, -1):
        flag = False
        temp = 0
        for j in range(m):
            if maps[i][j] == 1:
                if flag:
                    count += temp
                    temp = 0
                flag = True
            else:
                if flag:
                    temp += 1

    return count

# input
n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(solve(n, m, nums))