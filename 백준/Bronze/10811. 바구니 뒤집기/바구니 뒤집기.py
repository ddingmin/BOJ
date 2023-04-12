# input
n, m = map(int, input().split())
nums = []
for i in range(1, n + 1):
    nums.append(i)

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1 
    nums = nums[:a] + nums[a:b + 1][::-1] + nums[b + 1:]
print(*nums)