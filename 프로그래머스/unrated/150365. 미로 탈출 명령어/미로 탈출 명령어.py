# 이동 순서: ['d', 'l', 'r', 'u']

# 남은 거리 계산 함수
def calc_dist(x, y, r, c):
    return abs(x - r) + abs(y - c)

def solution(n, m, x, y, r, c, k):
    if (k - calc_dist(x, y, r, c)) % 2 or k < calc_dist(x, y, r, c):
        return "impossible"
    answer = ""
    move = 0
    # 아래로 최대한 이동
    while x < n and (k - move) > calc_dist(x, y, r, c):
        move += 1
        x += 1
        answer += "d"
    # 좌측으로 최대한 이동
    while 1 < y and (k - move) > calc_dist(x, y, r, c):
        move += 1
        y -= 1
        answer += "l"
        
    # 우좌 반복 이동
    while (k - move) > calc_dist(x, y, r, c):
        move += 2
        answer += "rl"
    
    # 가야할 길로 이동 dlru 순으로 이동
    if x < r:
        answer += "d" * (r - x)
        x = r
    if y > c:
        answer += "l" * (y - c)
        y = c
    if y < c:
        answer += "r" * (c - y)
        y = c
    if x > r:
        answer += "u" * (x - r)
        x = r
        

    return answer