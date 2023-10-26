# input
n, t, p = map(int, input().split())
p -= 1
arr = []

for idx in range(1, t + 1):
    a, b = input().split()
    arr.append([int(a[0:2]) * 60 + int(a[2:]) - 540, int(b[0:2]) * 60 + int(b[2:]) - 540])

arr = sorted(arr, key=lambda x: [x[0], x[1]])


##################################################

# func
def find_seat(seat, time):
    # 자리가 모두 비어 있는 경우
    count = 0
    for i in range(n):
        if seat[i][time] == 1:
            count += 1
    if count == 0:
        return 0

    temp_dist = 0
    temp_seat = 0
    for i in range(n):
        if seat[i][time] == 0:
            dis = 1
            while 1:
                left, right = i - dis, i + dis
                if (0 <= left < n) and seat[left][time] > 0:
                    if dis > temp_dist:
                        temp_dist = dis
                        temp_seat = i
                    break

                if (0 <= right < n) and seat[right][time] > 0:
                    if dis > temp_dist:
                        temp_dist = dis
                        temp_seat = i
                    break
                dis += 1

    return temp_seat


##################################################

# solve
seat = [[0] * 720 for _ in range(n)]

for start, end in arr:
    if start == end:
        continue
    target_seat = find_seat(seat, start)
    for i in range(start, end):
        seat[target_seat][i] = 1

answer = 0
for i in range(720):
    if seat[p][i] == 0:
        answer += 1

print(answer)
