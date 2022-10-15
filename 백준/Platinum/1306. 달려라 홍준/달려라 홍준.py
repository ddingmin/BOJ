from collections import deque

input = __import__('sys').stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
hongjun = m - 1
q = deque()
# 슬라이딩 윈도우 첫 값 설정 초기위치 m - 1에 시야 m - 1을 더한 값 까지 삽입
maxLight = arr[0]
secondLight = 0
cnt = [0] * (1000000 + 1)
cnt[arr[0]] += 1
q.append(arr[0])
ans = []
check = set()
check.add(arr[0])
for i in range(1, min(m - 1 + m, len(arr))):
    q.append(arr[i])
    check.add(arr[i])
    cnt[arr[i]] += 1
    if arr[i] > maxLight:
        secondLight = maxLight
        maxLight = arr[i]
    
ans.append(maxLight)

# 가장 밝은 빛이 나올때마다 cnt를 해주어 현재 윈도우에 maxLignt의 개수를 세어줌.
while 1:
    hongjun += 1
    out = q.popleft()
    cnt[out] -= 1
    if cnt[out] == 0:
        check.remove(out)
    if hongjun + m - 1 >= len(arr): break
    inn = arr[hongjun + m - 1]
    q.append(inn)
    check.add(inn)
    cnt[inn] += 1
    if inn > maxLight:
        maxLight = inn
    if cnt[maxLight] == 0:
        temp = sorted(list(check))
        if cnt[temp[-1]]: maxLight = temp[-1]
        else: maxLight = temp[-2]
        # for i in range(1, n):
        #     if cnt[maxLight - i] != 0: 
        #         maxLight = maxLight - i
        #         break
    ans.append(maxLight)
    if hongjun >= (n - m): break
print(*ans)