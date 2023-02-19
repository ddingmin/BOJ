import sys
import math
input = sys.stdin.readline

def solve(n, m):
    return m - math.gcd(n, m)

n, m = map(int, input().split())
print(solve(n, m))