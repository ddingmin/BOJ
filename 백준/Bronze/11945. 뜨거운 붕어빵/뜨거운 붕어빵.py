input = __import__('sys').stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(input().strip()))

for i in range(n):
    for j in range(m):
        print(arr[i][-1 * j - 1], end = '')
    print()
