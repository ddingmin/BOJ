import sys


def solve(p, arr):
    ans = 0
    for i in arr:
        if p >= i:
            ans += 1
            p -= i
        else:
            break
    return ans


def main():
    power = int(input())
    t = int(input())
    arr = list(int(input()) for _ in range(t))
    arr.sort()
    print(solve(power, arr))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
