import sys


def solve(n, cmds):
    answer = []

    start, end, cost = cmds[0]
    for s, e, c in cmds[1:]:
        if s <= end:
            end = max(end, e)
            cost = min(cost, c)
        else:
            answer.append([start, end, cost])
            start, end, cost = s, e, c

    answer.append([start, end, cost])
    print(len(answer))
    for pp in answer:
        print(*pp)


def main():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    solve(n, sorted(arr))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
