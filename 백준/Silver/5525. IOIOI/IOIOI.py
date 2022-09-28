input = __import__('sys').stdin.readline

n = int(input())
sm = int(input())
st = input().strip() + "A"

flag = 0
last = ""
cnt = 0
ans = 0
for i in range(sm + 1):
    if flag == 0 and st[i] == "I":
        flag = 1
    elif flag == 1 and last == "O" and st[i] == "I":
        cnt += 1
    elif flag == 1 and last == "I" and st[i] == "O":
        flag = 1
    else:
        flag = 0
        if cnt >= n:
            ans += 1 + cnt - n
        cnt = 0
        if st[i] == "I":
            flag = 1
    last = st[i]
print(ans)