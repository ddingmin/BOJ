import sys
input = sys.stdin.readline

def solve(n, k, nums):
    count = 0
    temp = 0
    psum = {0: 1}

    for num in nums:
        temp += num
        if temp - k in psum:
            count += psum[temp - k]
        
        if temp in psum:
            psum[temp] += 1
        else:
            psum[temp] = 1
    return count

n, k = map(int, input().split())
nums = list(map(int, input().split()))

print(solve(n, k, nums))