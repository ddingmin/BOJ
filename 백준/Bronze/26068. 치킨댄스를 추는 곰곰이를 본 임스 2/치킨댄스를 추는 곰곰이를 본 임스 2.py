answer = 0
for _ in range(int(input())):
    if int(input().strip()[2:]) <= 90:
        answer += 1
print(answer)
