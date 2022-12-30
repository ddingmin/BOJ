a, b = list(map(int, input().split()))
total = a * b
arr = list(map(int, input().split()))
for i in range(len(arr)):
    arr[i] -= total
print(*arr)