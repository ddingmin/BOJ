n = int(input())
nums = list(map(int, input().split()))
for i in range(n):
    nums[i] = [nums[i], i]

nums = sorted(nums)
answer = [0] * n
count = 0
for i in range(1, n):
    if nums[i][0] > nums[i - 1][0]:
        count += 1
    answer[nums[i][1]] = count

print(*answer)