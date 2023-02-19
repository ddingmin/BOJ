import sys
import math

input = sys.stdin.readline

def solve(a, b):
    return math.comb(b, a)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(solve(a, b))