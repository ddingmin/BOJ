from collections import deque


input = __import__('sys').stdin.readline
arr = deque()
sen = list(input().split())
for i in sen:
    arr.append(i[0].upper())

space = int(input())
key = list(map(int, input().split()))
cnt = 0

space -= len(sen) - 1

temp = ''
for i in arr:
    if temp != i:
        key[ord(i) - 65] -= 1
    temp = i

for i in sen:
    for j in i:
        if temp != j:
            if j.isupper():
                key[ord(j) - 65] -= 1
            else:
                key[ord(j) - 97] -= 1
        temp = j
flag = True
for i in range(len(key)):
    if key[i] < 0:
        flag = False
        break
if space < 0: flag = False

if flag: print("".join(arr))
else: print(-1)