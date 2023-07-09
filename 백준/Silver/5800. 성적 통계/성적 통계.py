import sys
input = sys.stdin.readline

for level in range(int(input())):
    nums = list(sorted(list(map(int, input().split()))[1:]))
    temp = 0

    for i in range(1, len(nums)):
        temp = max(temp, nums[i] - nums[i - 1])

    print(f"Class {level + 1}")
    print(f"Max {nums[-1]}, Min {nums[0]}, Largest gap {temp}")