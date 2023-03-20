import sys

input = sys.stdin.readline

def solve(n, nums):
    return (nums[-1] - nums[0]) * 2

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(n, sorted(nums)))
