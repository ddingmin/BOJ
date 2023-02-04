input = __import__('sys').stdin.readline
n = int(input())
arr = []
ans = 0

a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(n):
    arr.append([a[i],b[i]])
    
arr = sorted(arr, key = lambda x: [x[1]])

for i in range(n):
    ans += arr[i][0] + (i * arr[i][1])

print(ans)