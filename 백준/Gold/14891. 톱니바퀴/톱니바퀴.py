gear_1 = list(input())
gear_2 = list(input())
gear_3 = list(input())
gear_4 = list(input())

point_1, point_2, point_3, point_4 = 0, 0, 0, 0

n = int(input())

for _ in range(n):
    choice_gear, dir = map(int, input().split())
    if choice_gear == 1:
        if gear_1[(point_1 + 2) % 8] != gear_2[(point_2 + 6) % 8]: # 1번 톱니랑 2번 톱니가 달라서 회전.
            if gear_2[(point_2 + 2) % 8] != gear_3[(point_3 + 6) % 8]: # 2번 톱니와 3번 톱니가 달라서 회전
                if gear_3[(point_3 + 2) % 8] != gear_4[(point_4 + 6) % 8]: # 3번 톱니와 4번 톱니가 달라서 회전.
                    if dir == 1: point_4 += 1
                    else: point_4 += 7
                if dir == 1: point_3 += 7
                else: point_3 += 1
            if dir == 1: point_2 += 1
            else: point_2 += 7
        if dir == 1: point_1 += 7 # 시계방향
        else: point_1 += 1 # 반시계방향


    if choice_gear == 2:
        if gear_2[(point_2 + 2) % 8] != gear_3[(point_3 + 6) % 8]: # 2번 톱니랑 3번 톱니가 달라서 회전.
            if gear_3[(point_3 + 2) % 8] != gear_4[(point_4 + 6) % 8]: # 3번 톱니와 4번 톱니가 달라서 회전
                if dir == 1: point_4 += 7
                else: point_4 += 1
            if dir == 1: point_3 += 1
            else: point_3 += 7
        if gear_2[(point_2 + 6) % 8] != gear_1[(point_1 + 2) % 8]: # 2번 톱니와 1번 톱니가 달라서 회전.
            if dir == 1: point_1 += 1
            else: point_1 += 7
        if dir == 1: point_2 += 7 # 시계방향
        else: point_2 += 1 # 반시계방향


    if choice_gear == 3:
        if gear_3[(point_3 + 2) % 8] != gear_4[(point_4 + 6) % 8]: # 3번 톱니랑 4번 톱니가 달라서 회전.
            if dir == 1: point_4 += 1
            else: point_4 += 7
        if gear_3[(point_3 + 6) % 8] != gear_2[(point_2 + 2) % 8]: # 2번 톱니와 3번 톱니가 달라서 회전.
            if gear_1[(point_1 + 2) % 8] != gear_2[(point_2 + 6) % 8]: # 2번 톱니와 1번 톱니가 달라서 회전.
                if dir == 1: point_1 += 7
                else: point_1 += 1
            if dir == 1: point_2 += 1
            else: point_2 += 7

        if dir == 1: point_3 += 7 # 시계방향
        else: point_3 += 1 # 반시계방향


    if choice_gear == 4:
        if gear_4[(point_4 + 6) % 8] != gear_3[(point_3 + 2) % 8]: # 4번 톱니랑 3번 톱니가 달라서 회전.
            if gear_3[(point_3 + 6) % 8] != gear_2[(point_2 + 2) % 8]: # 2번 톱니와 3번 톱니가 달라서 회전
                if gear_2[(point_2 + 6) % 8] != gear_1[(point_1 + 2) % 8]: # 2번 톱니와 1번 톱니가 달라서 회전.
                    if dir == 1: point_1 += 1
                    else: point_1 += 7
                if dir == 1: point_2 += 7
                else: point_2 += 1
            if dir == 1: point_3 += 1
            else: point_3 += 7
        if dir == 1: point_4 += 7 # 시계방향
        else: point_4 += 1 # 반시계방향
    point_1 %= 8
    point_2 %= 8
    point_3 %= 8
    point_4 %= 8

ans = 0
if gear_1[point_1] == '1': ans += 1
if gear_2[point_2] == '1': ans += 2
if gear_3[point_3] == '1': ans += 4
if gear_4[point_4] == '1': ans += 8
print(ans)