#input = __import__('sys').stdin.readline

n = input()

cnt = [0] * 11
for i in range(len(n)):
    if int(n[i]) == 6 or int(n[i]) == 9:
        cnt[6] += 1
    else: cnt[int(n[i])] += 1
cnt[6] /= 2
if cnt[6] != int(cnt[6]): cnt[6] = int(0.5 + cnt[6])
print(int(max(cnt)))
