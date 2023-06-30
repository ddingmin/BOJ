n, c = map(int, input().split())
d = {}
idx = 0
for i in list(map(int, input().split())):
    if not i in d:
        d[i] = [1, idx]
        idx += 1
    else:
        d[i][0] += 1

answer = []
temp = []
for i in d:
    for _ in range(d[i][0]):
        temp.append([d[i][0], d[i][1], i])

temp = sorted(temp, key = lambda x: [-x[0], x[1]])
for i in range(len(temp)):
    answer.append(temp[i][2])

print(*answer)