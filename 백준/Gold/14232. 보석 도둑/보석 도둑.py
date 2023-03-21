import sys
import math

input = sys.stdin.readline

def solve(n):
    answer = []
    target = int(math.sqrt(n)) + 1
    for i in range(2, target + 1):
        while n % i == 0:
            answer.append(i)
            n //= i
    if n != 1: answer.append(n)
    print(len(answer))
    return answer

n = int(input())
print(*solve(n))
