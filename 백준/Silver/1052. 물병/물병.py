import sys
input = sys.stdin.readline

def solve(n, k):
    count = 0
    while bin(n).count('1') > k:
        count += 1
        n += 1
    return count

n, k = map(int, input().split())
print(solve(n, k))