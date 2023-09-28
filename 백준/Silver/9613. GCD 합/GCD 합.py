import sys
import math
from itertools import combinations as cb
from itertools import permutations as pm
from collections import deque


sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# input
n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    temp = 0

    for j in range(1, len(arr)):
        for k in range(j + 1, len(arr)):
            temp += math.gcd(arr[j], arr[k])
    print(temp)