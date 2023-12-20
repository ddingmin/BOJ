import sys

MAX_VALUE = 1_000_000


def solve(size, arr):
    cnt = [0] * (MAX_VALUE + 1)
    ans = 0

    for i in arr:
        if cnt[i]:
            cnt[i] -= 1
        else:
            ans += 1

        cnt[i - 1] += 1

    return ans


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
