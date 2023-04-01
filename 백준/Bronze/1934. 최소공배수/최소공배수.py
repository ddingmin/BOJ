import sys
import heapq
from collections import deque
from bisect import bisect_left
import math
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

# input
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))
