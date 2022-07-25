t = input()
ans = 0
number = ''
flag = '+'
for k in t:
    if k == '+' or k == '-':
        if flag == '-':
            ans -= int(number)
        elif k == '-':
            ans += int(number)
            flag = '-'
        elif k == '+':
            ans += int(number)
        number = ''
    else:
        number += k
if flag == '-':
    ans -= int(number)
else:
    ans += int(number)

print(ans)