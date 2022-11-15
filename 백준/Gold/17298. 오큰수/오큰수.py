n = int(input())
arr = list(map(int, input().split()))

nums = []
for i in range(len(arr)):
    nums.append((i, arr[i]))

ans = [-1] * n
stack = [nums[0]]

for i in range(1, len(nums)):
    idx, value = stack[-1]
    if value < nums[i][1]:
        while stack and (stack[-1][1] < nums[i][1]):
            iidx, vvalue = stack.pop()
            ans[iidx] = nums[i][1]
    
    stack.append(nums[i])

print(*ans)