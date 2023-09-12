import sys

input = sys.stdin.readline

target = 'DKSH'
word = input().strip()

ans = 0
if word == target:
    print(1)
    exit()

for i in range(len(word) - 3):
    temp = word[i:i + 4]
    if temp == target:
        ans += 1

print(ans)