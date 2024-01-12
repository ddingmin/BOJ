import sys


def solve(arr):
    return sorted(arr)[0][1]


def main():
    n = int(input())
    while n:
        arr = []
        for i in range(n):
            word = input().strip()
            arr.append([word.upper(), word])
        print(solve(arr))
        n = int(input())


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
