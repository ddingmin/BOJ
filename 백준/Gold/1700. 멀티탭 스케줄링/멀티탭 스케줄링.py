n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))


# 몇 번 이후에 도착하는지 체크하는 배열
visit = [[float('inf')] * 101 for _ in range(101)]

# i번 위치에 존재하는 전기용품의 다음 index를 구하기
for i in range(1, k + 1):
    prev = -1
    for idx in range(1, len(arr)):
        now = arr[idx]
        if i == now:
            if prev == -1:
                prev = idx
            else:
                visit[i][prev] = idx
                prev = idx

def inn(idx, now):
    global concent_count
    global ans

    # 이미 꼽혀있다면 idx 갱신
    if concent[now]:
        concent[now] = idx
        return
    # 꼽힐 공간이 남아있다면 꼽고 idx 갱신
    elif concent_count < concent_max:
        concent[now] = idx
        concent_count += 1
        return

    # 뽑아야 하는 경우
    else:
        length = 0
        found = 0
        # 꽃혀있는 전기용품을 찾아 다음 index가 가장 뒤에 있는 전기용품을 뽑기
        for i in range(1, 101):
            if concent[i]:
                found += 1
                if visit[i][concent[i]] > length:
                    length = visit[i][concent[i]]
                    getout = i
                if found == concent_max: break
        # 뽑은건 idx 0 으로 갱신, 꼽은것 idx 갱신
        concent[getout] = 0
        concent[now] = idx
        ans += 1
        return

ans = 0
concent = [0] * 101
concent_count = 0
concent_max = n

for i in range(1, len(arr)):
    now = arr[i]
    inn(i, now)

print(ans)