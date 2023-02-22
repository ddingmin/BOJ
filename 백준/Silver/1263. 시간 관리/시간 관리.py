def solve(n, nums):
    answer = float('inf')
    nums.sort(key = lambda x: [-x[1], -x[0]])
    for t, s in nums:
        answer = min(s - t, answer - t)
    if answer < 0:
        return -1
    return answer
    
n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, nums))