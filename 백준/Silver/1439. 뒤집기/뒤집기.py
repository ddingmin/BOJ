input = __import__('sys').stdin.readline
s = input().strip()
ans = 0
flag = s[0]
for i in range(1, len(s)):
    if flag == s[i]: continue
    else:
        flag = s[i]
        ans += 1
print((ans + 1) // 2)
