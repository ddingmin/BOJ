import sys
input = sys.stdin.readline

n = int(input())
answer = []

for _ in range(n):
    line = input().strip()
    temp = ""
    for i in line:
        if i.isdecimal():
            if len(temp):
                temp += i
            else:
                temp = i
        else:
            if len(temp):
                answer.append(int(temp))
            temp = ""
    if len(temp):
        answer.append(int(temp))

for n in sorted(answer):
    print(n)
