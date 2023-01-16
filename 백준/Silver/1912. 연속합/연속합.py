n = int(input())

arr = list(map(int, input().split()))

ans = max(arr)
temp = 0
for i in arr:
    temp += i
    ans = max(ans, temp)
    
    if temp < 0:
        temp = 0
        continue
print(ans)