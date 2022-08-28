# input
input = __import__('sys').stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

total = 0
cnt = 0
temp = 0
for i in range(0, len(arr)):
    temp = max(temp, arr[i])
    total += arr[i]
if total == 1: print("Happy")
else:
    if temp > (total // 2): print("Unhappy")
    else: print("Happy")