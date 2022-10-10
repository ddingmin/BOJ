n = int(input())
temp = 1
ans = 0
s = 1
for i in range(1, n + 1):
    temp *= i
    s *= i
    check = str(temp)
    cnt = 0
    for j in range(len(check)):
        if check[-j - 1] == '0': 
            ans += 1
            cnt += 1
        else: 
            temp //= 10 ** cnt
            while temp % 10 == 0:
                temp //= 10
            break
print(ans)