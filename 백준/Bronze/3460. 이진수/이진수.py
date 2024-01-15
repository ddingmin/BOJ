import sys


def solve(n):
    n = bin(n)[2:]

    ans = []
    for i in range(len(n)):
        if n[i] == '1':
            ans.append(len(n) - i - 1)

    print(*sorted(ans))


def main():
    t = int(input())
    for _ in range(t):
        solve(int(input()))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
