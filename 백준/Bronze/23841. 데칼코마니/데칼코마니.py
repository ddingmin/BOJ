# input
input = __import__('sys').stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(input().strip()))
    for j in range(m):
        if arr[i][j] != '.': arr[i][-(j + 1)] = arr[i][j]

for k in arr:
    print("".join(map(str, k)))