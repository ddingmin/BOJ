import sys
input = sys.stdin.readline

k, l = map(int, input().split())
order = {}
snums = {}
idx = 1
for _ in range(l):
    snum = input().strip()
    
    snums[snum] = idx
    order[idx] = snum
    idx += 1

answer = []
for i in range(1, len(order) + 1):
    if i == snums[order[i]]:
        answer.append(order[i])


for i in range(min(k, len(answer))):
    print(answer[i])
