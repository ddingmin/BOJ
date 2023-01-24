n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))
num = sorted(num)

# 산술 평균
print(round(sum(num) / len(num)))
# 중앙값
print(num[len(num) // 2])
# 최빈값
least = [[0, 0]]
count = 1
temp = num[0]
for i in range(1, len(num)):
    if temp != num[i]:
        if count > least[0][1]:
            least = [[temp, count]]
        elif count == least[0][1]:
            least.append([temp, count])
        temp = num[i]
        count = 1
    else:
        count += 1
if count > least[0][1]:
    least = [[temp, count]]
elif count == least[0][1]:
    least.append([temp, count])
least.sort()
if len(least) > 1:
    print(least[1][0])
else:
    print(least[0][0])

# 볌위
print(max(num) - min(num))