n = int(input())
arr = list(map(int, input().split()))
arr.append(0)
score = 1
ans = 0
flag = False

for i in range(n):
    if arr[i] == 1:
        if flag:
            score += 1
        ans += score
        flag = True
    else:
        flag = False
        score = 1
print(ans)