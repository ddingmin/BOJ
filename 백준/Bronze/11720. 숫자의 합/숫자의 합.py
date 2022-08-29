# input
input = __import__('sys').stdin.readline
n = int(input())
arr = list(map(int, list(input().strip())))
print(sum(arr))