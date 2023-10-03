import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [1, 0], [0, 1]

# input
c = input().strip()

d = {'M': "MatKor",
     'W': "WiCys",
     'C': "CyKor",
     'A': "AlKor",
     '$': "$clear"}
print(d[c])
