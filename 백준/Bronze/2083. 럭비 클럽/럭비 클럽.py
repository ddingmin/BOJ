import sys
input = sys.stdin.readline

def solve(n, nums):
    mid = n // 2
    new = [nums[mid]]
    for i in range(n):
        if i == mid: continue
        new.append(nums[i])
    new.append(nums[mid])
    answer = 0
    for i in range(1, len(new)):
        answer = max(answer, abs(new[i] - new[i - 1]))
    return answer

while 1:
    t = list(input().split())
    if t[0] == '#' and t[1] == '0' and t[2] == '0': break
    if int(t[1]) > 17 or int(t[2]) >= 80:
        print(t[0], "Senior")
    else:
        print(t[0], "Junior")
    