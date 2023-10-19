import sys
from collections import deque
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
dx, dy = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]

# input
n = int(input())
arr = sorted(list(map(int, input().split())))
total = int(input())

start, end = 0, max(arr)
answer = 0

if total >= sum(arr):
    print(max(arr))
    exit()

while start <= end:
    mid = (start + end) // 2
    temp = 0

    for i in range(n):
        temp += min(arr[i], mid)

    if temp <= total:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)
