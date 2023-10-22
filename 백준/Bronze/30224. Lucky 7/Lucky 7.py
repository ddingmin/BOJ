import sys
from collections import deque
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
# dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

# solve

# input
n = int(input())

sn = str(n)
if not '7' in sn and n % 7 != 0:
    print(0)
elif not '7' in sn and n % 7 == 0:
    print(1)
elif '7' in sn and n % 7 != 0:
    print(2)
elif '7' in sn and n % 7 == 0:
    print(3)
