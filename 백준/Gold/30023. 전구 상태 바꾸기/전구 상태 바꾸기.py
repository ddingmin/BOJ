import sys
from collections import deque
from bisect import bisect_left, bisect_right
import heapq

# sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

# dx = [-1, 0, 1]
# dx, dy = [0, 1], [1, 0]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
# dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

# input
n = int(input())
arr = list(input().strip())

change = {'R': 'G', 'G': 'B', 'B': 'R'}


def change_light(idx, arr):
    arr[idx], arr[idx + 1], arr[idx + 2] = change[arr[idx]], change[arr[idx + 1]], change[arr[idx + 2]]
    return arr


def solve(new_arr):
    count = 0

    for i in range(1, n - 2):
        while new_arr[0] != new_arr[i]:
            count += 1
            new_arr = change_light(i, new_arr)

    if new_arr[0] == new_arr[-1] == new_arr[-2]:
        return count
    return -1

answer = float('inf')

for i in range(3):
    temp = solve(arr.copy())
    arr = change_light(0, arr)
    if temp != -1:
        answer = min(answer, temp + i)
if answer == float('inf'):
    answer = -1
print(answer)
