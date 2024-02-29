n, m, k = map(int, input().split())

# 인턴쉽에 참여하는 여자 수: a (0~k) 남자: k - a


ans = 0

for a in range(0, k + 1):
    # 인턴쉽에 참여한 남자 수: b
    b = k - a

    # 대회에 참여할 수 있는 남녀 수
    girl, boy = n - a, m - b

    if girl < 0 or boy < 0:
        continue

    team = min(girl // 2, boy)

    ans = max(ans, team)

print(ans)
