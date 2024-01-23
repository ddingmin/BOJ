import sys
import math


def solve(origin, arr):
    pass


def main():
    a, b, c = map(int, input().split())
    a_team = list(input().split())
    b_team = list(input().split())

    man = {}

    for a in a_team:
        man[a] = 0
    for b in b_team:
        man[b] = 1

    goal = list(input().split())

    score = [0, 0]

    for g in goal:
        score[man[g]] += 1

    if score[0] > score[1]:
        print('A')
    elif score[0] < score[1]:
        print('B')
    else:
        print("TIE")


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
