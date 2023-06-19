import sys
import math

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0
for i in range(n):
    arr[i] -= b
    answer += 1
    if arr[i] > 0:
        answer += math.ceil(arr[i] / c)

print(answer)