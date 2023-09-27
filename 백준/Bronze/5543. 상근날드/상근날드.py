import sys
from itertools import combinations as cb
from itertools import permutations as pm
from collections import deque

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# input
a = min(list(int(input()) for _ in range(3)))
b = min(list(int(input()) for _ in range(2)))

print(a + b - 50)
