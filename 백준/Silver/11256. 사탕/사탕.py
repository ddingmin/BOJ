import sys


def solve(candy, boxes):
    ans = 0

    for i in boxes:
        if candy > 0:
            candy -= i
            ans += 1
        else:
            break

    return ans


def main():
    t = int(input())
    for _ in range(t):
        candy, box = map(int, input().split())
        boxes = []
        for _ in range(box):
            a, b = map(int, input().split())
            boxes.append(a * b)
        boxes.sort(reverse=True)
        print(solve(candy, boxes))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
