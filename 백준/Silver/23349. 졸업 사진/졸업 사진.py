input = __import__('sys').stdin.readline

n = int(input())

def solve():
    student = {}
    place = {}
    timeList = []
    placeIdx = 0
    
    highTime = 0    # 가장 사람이 많을때의 사람 수
    for _ in range(n):
        name, p, s, e = input().split()
        s, e = int(s), int(e)
        # 학생 중복제출 체크
        if name in student: continue
        else: student[name] = 1
        # 장소 중복 체크
        if p not in place:  # 장소가 이미 존재하지 않는다면
            place[p] = placeIdx
            placeIdx += 1
            temp = [0] * 50002
            # 시간 채우기 & 최대 사람 수 갱신
            for i in range(s, e):
                temp[i] += 1
                highTime = max(highTime, temp[i])
            timeList.append(temp)
        else:   # 장소가 이미 존재한다면
            # 시간 채우기 & 최대 사람 수 갱신
            for i in range(s, e):
                timeList[place[p]][i] += 1
                highTime = max(highTime, timeList[place[p]][i])
    # 사전순으로 정렬 후 탐색 -> 가장 빨린 찾은 구간이 답
    key = sorted(place.keys())
    ans = []
    for k in key:
        isFind = False
        for i in range(50002):
            # 시작 구간을 찾았을 경우
            if timeList[place[k]][i] == highTime and isFind == False:
                ans.append(k)
                ans.append(i)
                isFind = True
            # 종료 구간을 찾았을 경우
            elif isFind and timeList[place[k]][i] != highTime:
                ans.append(i)
                return ans

print(*solve())