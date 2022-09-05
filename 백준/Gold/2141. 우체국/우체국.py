# input
input = __import__('sys').stdin.readline

def solve(cnt, arr):
    arr = sorted(arr)
    if cnt % 2 == 1: idx = cnt // 2 + 1
    else: idx = cnt // 2 - 1
    for i, j in arr:
        idx -= j
        
        if idx <= 0:
            return i

# main
n = int(input())
arr = []
cnt = 0
for _ in range(n):
    x, people = map(int, input().split())
    cnt += people
    arr.append((x, people))

# Output
print(solve(cnt, arr))