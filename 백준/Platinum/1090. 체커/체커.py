input = __import__('sys').stdin.readline

# 1 ~ n 개를 골라 맨해튼 거리가 최소가 되는 좌표의 최소 거리를 구하여라

n = int(input())
arr = []
_xarr = []
_yarr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
    _xarr.append(a)
    _yarr.append(b)

ans = [-1] * n

# 맨해튼 거리는 어차피 받은 배열안에 존재하기 때문에 배열만 확인하면 된다.
for sx in _xarr:
    for sy in _yarr:
        # 각 좌표에 대한 거리를 모아 놓는다.
        dist = []
        for ex, ey in arr:
            d = abs(ex - sx) + abs(ey - sy)
            dist.append(d)
        # 내림차순 정렬
        dist.sort()
        
        # 1 ~ N개 선택했을 때 최소 이동 횟수를 ans에 갱신해준다.
        temp = 0
        for i in range(len(dist)):
            d = dist[i]
            temp += d
            if ans[i] == -1: ans[i] = temp
            else: ans[i] = min(temp, ans[i])

print(*ans)