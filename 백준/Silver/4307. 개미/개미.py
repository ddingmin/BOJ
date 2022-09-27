# 4307 개미
input = __import__('sys').stdin.readline

def solve(l, arr):
    m = l // 2
    short = 0
    long = 0
    for value in arr:
        if value > m:
            short = max(short, l - value)
            long = max(long, value)
        else:
            short = max(short, value)
            long = max(long, l - value)
    return short, long

input = __import__('sys').stdin.readline
t = int(input())

for _ in range(t):
    l, n = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    
    print(*solve(l, arr))