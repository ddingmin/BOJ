n = int(input())
arr = sorted(list(map(int, input().split())))
if n == 1: print(arr[0])
else: print(arr[(len(arr) - 1) // 2])
