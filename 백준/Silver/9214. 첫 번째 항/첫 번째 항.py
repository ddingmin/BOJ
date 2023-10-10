import sys
import math
from itertools import combinations as cb
from itertools import permutations as pm
from collections import deque

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dx, dy = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, -2, -1, 1, 2]


# solve
def game(cur):
    while 1:
        if len(cur) % 2 == 1:
            return cur
        next = []
        for i in range(len(cur) // 2):
            for _ in range(cur[i * 2]):
                next.append(cur[i * 2 + 1])
        if next == cur:
            return cur
        cur = next


# input
idx = 1
while 1:
    start = list(map(int, list(input().strip())))
    if len(start) == 1 and start[0] == 0:
        break
    result = game(start)
    print(f"Test {idx}: " + "".join(map(str, result)))
    idx += 1

