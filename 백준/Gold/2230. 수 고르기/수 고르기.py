input = __import__('sys').stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))    
arr.sort()

ans = float('inf')

left, right = 0, 0
while left < len(arr) and right < len(arr):
    if left >= right:
        right += 1
        continue
    if arr[right] - arr[left] >= m:
        ans = min(ans, arr[right] - arr[left])
        left += 1
        continue
    else:
        right += 1

print(ans)
