import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

# input
n = int(input())
arr = list(input().split())

cheese = {}
for word in arr:
    if len(word) >= 6 and word[-6:] == "Cheese":
        cheese[word] = 1
if len(cheese) >= 4:
    print("yummy")
else:
    print("sad")
