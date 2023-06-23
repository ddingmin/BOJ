import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = []
words = []
for i in range(n):
    arr.append(list(input().strip()))
    temp = ""
    for j in range(m):
        if arr[i][j] != "#":
            temp += arr[i][j]
        else:
            if len(temp) > 1:
                words.append(temp)
            temp = ""
    if len(temp) > 1:
        words.append(temp)

for j in range(m):
    temp = ""
    for i in range(n):
        if arr[i][j] != "#":
            temp += arr[i][j]
        else:
            if len(temp) > 1:
                words.append(temp)
            temp = ""
    if len(temp) > 1:
        words.append(temp)
print(sorted(words)[0])