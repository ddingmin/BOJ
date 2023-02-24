import sys
input = sys.stdin.readline

def isAns(nums):
    if int(str(nums)[0]) - int(str(nums)[1]) == int(str(nums)[1]) - int(str(nums)[2]):
        return 1
    else: return 0

def solve(n):
    isanswer = [0] * 1001
    for i in range(1, 100):
        isanswer[i] = 1
    for num in range(100, 1000):
        isanswer[num] = isAns(num)
    return sum(isanswer[:n + 1])

n = int(input())
print(solve(n))