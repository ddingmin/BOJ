line = input()
ans = 0
for i in range(len(line)):
    if line[i] == 'U' and ans == 0:
        ans += 1
    elif line[i] == 'C' and ans == 1:
        ans += 1
    elif line[i] == 'P' and ans == 2:
        ans += 1
    elif  line[i] == 'C' and ans == 3:
        ans += 1
if ans == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")