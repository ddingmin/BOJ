def solve(n, nums):
    result = {}
    # x + y = k - z 가 되어야 함.
    answer = -1
    for x in nums:
        for y in nums:
            result[x + y] = True
    for k in nums:
        for z in nums:
            if k - z in result:
                answer = max(answer, k)
    return answer

n = int(input())
nums = [int(input()) for _ in range(n)]
print(solve(n, nums))