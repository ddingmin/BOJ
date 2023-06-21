from collections import deque
# 과제는 시간이 되면 시작한다.
# 새로운 과제가 시작할 시간이 되면 진행중인 과제는 중단하고 새로운 과제를 시작한다.
# 중단된 과제는 스택으로 관리한다.
# 과제를 끝냈을 경우, 시작할 과제가 있다면 시작, 중단된 과제가 있다면 재시작한다.

# 분 단위로 모두 바꿔서 구현

def convert(plans):
    temp = []
    for name, time, playtime in plans:
        hh, mm = time.split(':')
        mm = int(hh) * 60 + int(mm)
        playtime = int(playtime)
        temp.append([mm, playtime, name])
    return deque(sorted(temp))

def do(plans):
    time = plans[0][0]
    finished = []
    stop = []
    doing = []
    
    while plans or doing or stop:
        # 새 할일 시간이 된 경우
        if plans and plans[0][0] == time:
            # 작업중인게 있는 경우
            if doing:
                end, name = doing
                # 작업이 끝난 경우
                if time == end:
                    finished.append(name)
                else:
                    stop.append([end - time, name])
            start, left, name = plans.popleft()
            doing = [start + left, name]
    
        if doing and doing[0] == time:
            finished.append(doing[1])
            doing = []
            if stop:
                left, name = stop.pop()
                doing = [time + left, name]
            
        time += 1
    return finished


def solution(plans):
    plans = convert(plans)
    return do(plans)