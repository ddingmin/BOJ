import sys
from itertools import combinations as cb
from itertools import permutations as pm
from collections import deque

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1, 0, -1):
    if arr[i - 1] > arr[i]:
        target = i - 1
        break
else:
    print(-1)
    sys.exit()

for i in range(n - 1, 0, -1):
    if arr[i] < arr[target]:
        arr[i], arr[target] = arr[target], arr[i]
        break
ans = arr[:target + 1] + sorted(arr[target + 1:], reverse=True)
print(*ans)
