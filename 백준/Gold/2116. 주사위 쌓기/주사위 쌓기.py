import sys
import heapq
import math
from collections import deque
from bisect import bisect_left
input = sys.stdin.readline

match = [5, 3, 4, 1, 2, 0]
def solve(n, dices):
    answer = 0
    # 주사위 1, 6을 바닥으로 두어 완탐
    for top in range(6):
        down = match[top]
        prev_top = dices[0][top]
        temp = 0
        for i in range(6):
            # 위 아래 주사위 스킵
            if i == top or i == down: continue
            temp = max(temp, dices[0][i])
        score = temp
        
        
        for i in range(1, n):
            # 이전 주사위의 top
            dice = dices[i]
            # 가장 아래 주사위의 index 구하기
            for i in range(6):
                if dice[i] == prev_top:
                    down = i
                    top = match[i]
                    break
            
            temp = 0
            for i in range(6):
                if i == top or i == down: continue
                temp = max(temp, dice[i])
            score += temp
            prev_top = dice[top]
        answer = max(answer, score)
    return answer

n = int(input())
dices = []
for _ in range(n):
    dices.append(list(map(int, input().split())))

print(solve(n, dices))