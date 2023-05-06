import math
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

print(sum(nums) / n)
if n % 2 == 0:
    print((nums[n // 2] + nums[n // 2 - 1]) / 2)
else:
    print(nums[n // 2])