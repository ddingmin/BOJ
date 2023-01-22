n = int(input())
arr = []
for _ in range(n):
    a, b = input().split()
    arr.append([int(a), b])
arr = sorted(arr, key= lambda x: [x[0]])
for x, y in arr:
    print(x, y)