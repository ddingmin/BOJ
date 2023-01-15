input = __import__('sys').stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = 0
temp = 0

for i in range(len(arr)):
    if arr[i] == 1:
        temp += 1
    else:
        temp -= 1
    ans = max(ans, temp)
    if temp < 0:
        temp = 0

temp = 0

for i in range(len(arr)):
    if arr[i] == 1:
        temp -= 1
    else:
        temp += 1
    ans = max(ans, temp)
    if temp < 0:
        temp = 0

print(ans)