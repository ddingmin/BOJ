n = int(input())
arr = list(map(int, input().split()))

cnt = 0

while sum(arr):
    for i in range(len(arr)):
        if arr[i] == 0: continue
        elif arr[i] == 1: 
            cnt += 1
            arr[i] = 0
        elif arr[i] % 2 == 1:
            arr[i] -= 1
            cnt += 1
    if sum(arr) == 0: break
    for i in range(len(arr)):
        arr[i] //= 2
    cnt += 1
print(cnt)