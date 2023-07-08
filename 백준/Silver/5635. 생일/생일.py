input = __import__('sys').stdin.readline

n = int(input())
arr = []

for _ in range(n):
    a, b, c, d = input().split()
    arr.append([int(d), int(c), int(b), a])

arr.sort()

print(arr[-1][-1])
print(arr[0][-1])
