input = __import__('sys').stdin.readline

n = int(input())
arr = [[0, 0] for _ in range(46)]

arr[1] = [0, 1]
for i in range(2, 46):
    arr[i][0], arr[i][1] = arr[i - 1][1], arr[i - 1][1] + arr[i - 1][0]
print(*arr[n])