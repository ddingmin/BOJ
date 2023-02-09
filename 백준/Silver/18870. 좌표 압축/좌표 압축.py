n = int(input())
nums = list(map(int, input().split()))
ordering_nums = sorted(set(nums))
answer = {}

count = 0
for i in ordering_nums:
    answer[i] = count
    count += 1

for i in nums:
    print(answer[i], end = " ")