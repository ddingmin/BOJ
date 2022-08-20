from collections import deque

# input
input = __import__('sys').stdin.readline
n = int(input())
crain = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crain = sorted(crain, reverse= True)
box = sorted(box, reverse= True)

cnt = 0
if crain[0] < box[0]: print(-1)
else:
    while sum(box) > 0:
        idx = 0
        for k in range(m):
            # 크레인을 다 사용
            if not(0 <= idx < n): break
            
            # 해당 박스 이미 옮김
            if box[k] == 0: continue

            # 옮길 수 있을 때
            if box[k] <= crain[idx]:
                idx += 1
                box[k] = 0
            else:
                continue
        cnt += 1

    print(cnt)