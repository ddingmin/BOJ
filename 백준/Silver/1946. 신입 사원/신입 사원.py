input = __import__('sys').stdin.readline
t = int(input())
for i in range(t):
    arr = []
    n = int(input())
    for j in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr = sorted(arr, key = lambda x: [x[0]])
    ans = n
    temp = arr[0][1]
    for j in range(1, len(arr)):
        if arr[j][1] < temp:
            temp = arr[j][1]
        else:
            ans -= 1
    print(ans)