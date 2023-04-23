import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))
belt = deque(temp)
robots = deque([0] * (n * 2))
TAKE, OUT = 0, n - 1

def out_robot():
    robots[OUT] = 0

def location():
    belt.appendleft(belt.pop())
    robots.appendleft(robots.pop())
    out_robot()

def robot_move():
    for i in range(OUT - 1, -1, -1):
        cur = i
        next = i + 1
        if robots[cur] == 1:
            if belt[next] > 0 and robots[next] == 0:
                belt[next] -= 1
                robots[next], robots[cur] = 1, 0
    out_robot()

def robot_take():
    if robots[TAKE] == 0 and belt[TAKE] > 0:
        belt[TAKE] -= 1
        robots[TAKE] = 1

def check_zero():
    count = 0
    for i in range(n * 2):
        if belt[i] == 0:
            count += 1
    if count >= k:
        return False
    else:
        return True

answer = 1
while 1:
    location()
    robot_move()
    robot_take()

    if check_zero():
        answer += 1
    else:
        break
print(answer)
    