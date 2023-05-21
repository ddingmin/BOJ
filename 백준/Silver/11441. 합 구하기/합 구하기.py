import sys

input = sys.stdin.readline
######################### solve ###############################


def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    psum = [0]
    for i in nums:
        psum.append(psum[-1] + i)
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(psum[b] - psum[a - 1])


###############################################################

solve()
