import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# input
n = int(input())

for i in range(n * 4):
    print("@" * n)
for i in range(n):
    print("@" * (n * 5))
