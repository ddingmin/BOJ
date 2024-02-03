import sys


def solve(n, arr):
    ans = 0
    target = []
    for i in range(1, n + 1):
        target.append(i)

    for i in range(n):
        if target[i] != arr[i]:
            ans += 1
    return ans


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
