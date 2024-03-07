import sys

n = int(input())
arr = sys.stdin.read().rstrip()
total = 0

temp = ""
for a in arr:
    if a.isdigit():
        temp += a
    elif a == " ":
        total += int(temp)
        temp = ""
total += int(temp)

target = n * (n + 1) // 2

print(n - (target - total))