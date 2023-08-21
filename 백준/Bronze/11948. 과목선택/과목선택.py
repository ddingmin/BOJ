ans = 0
temp = []
for _ in range(4):
    temp.append(int(input()))

temp2 = []
for _ in range(2):
    temp2.append(int(input()))

ans += sum(sorted(temp)[1:])
ans += sum(sorted(temp2)[1:])

print(ans)