import sys

input = sys.stdin.readline

def isAnswer(nums, new):
    for i in nums:
        if i not in new:
            return 0
    return 1
    

def solve(n, nums):
    s = set()
    for i in nums:
        s.add(i)
        for j in nums:
            if j - i >= 0:
                s.add(j - i)
    count = 0
    new = []
    for a in s:
        for b in s:
            for c in s:
                if not(a <= b <= c): continue
                new.append(a)
                new.append(b)
                new.append(c)
                new.append(a + b)
                new.append(a + c)
                new.append(b + c)
                new.append(a + b + c)
                count += isAnswer(nums, new)
                new.clear()
    
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve(n, nums))