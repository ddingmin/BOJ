n = list(map(int, list(input())))
cnt = 0
while len(n) != 1:
    cnt += 1
    temp = sum(n)
    n = list(map(int, (list(str(temp)))))

n = n[0]
print(cnt)
if n % 3 == 0:
    print("YES")
else:
    print("NO")