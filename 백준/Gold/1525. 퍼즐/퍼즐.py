from collections import deque

# input
input = __import__('sys').stdin.readline
arr = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = "123456780"
for i in range(3):
    arr.append(list(map(int, input().split())))
    for j in range(3):
        # 0의 좌표 구하기
        if arr[i][j] == 0: start = (i, j)

def makeVisit(visit):
    string = ""
    for i in range(3):
        string += "".join(map(str, visit[i]))
    return string

def makeArr(string):
    temp = [[0] * 3 for _ in range(3)]
    k = 0
    for i in range(3):
        for j in range(3):
            temp[i][j] = string[k]
            k += 1
    return temp

def solve():
    global arr
    q = deque()
    visit = {}
    temp = makeVisit(arr)
    if temp == ans:
        return 0
    visit[temp] = 1
    i, j = start
    # 0의 좌표와 배열, 이동 횟수를 받음.
    q.append((i, j, temp, 0))

    while q:
        i, j, mp, c = q.popleft()
        for k in range(4):
            # 문자열 형태 -> 배열 형태로 변환
            arr = makeArr(mp)

            x, y = i + dx[k], j + dy[k]     # 0의 위치와 바꿀 좌표
            if not(0 <= x < 3 and 0 <= y < 3): continue

            # 바꾸기
            arr[x][y], arr[i][j] = arr[i][j], arr[x][y]
            temp = makeVisit(arr)

            # 정답 리스트와 일치하면 반환
            if temp == ans: return c + 1

            # 방문 배열 확인
            if temp in visit: continue
            else: 
                visit[temp] = 1
                q.append((x, y, temp, c + 1))
    return -1

print(solve())