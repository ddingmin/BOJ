n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key = lambda x : [x[1], x[0]])
for k in arr:
    print(*k)
