import sys

input = sys.stdin.readline

t = int(input())

def solve(n):
    if n == 0:
        return "INSOMNIA"
    num = {}
    idx = 1
    while 1:
        new = str(n * idx)
        for i in new:
            num[i] = 1
        if len(num) == 10:
            return new
        idx += 1


for case in range(1, t + 1):
    n = int(input())
    print(f"Case #{case}: {solve(n)}")
