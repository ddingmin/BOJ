import sys
import heapq
import math
input = sys.stdin.readline

def solve(scores):
    psum = 0
    answer = []
    for i in range(5):
        score, i = scores[i]
        psum += score
        answer.append(i)
    print(psum)
    print(*sorted(answer))
    return 

scores = []
for i in range(1, 9):
    score = int(input())
    scores.append([score, i])

solve(sorted(scores, reverse= 1))