import sys


def solve(n, arr):
    flag = True

    for i in range(n):
        name = arr[i][0]
        for j in range(1, len(arr[i])):
            if arr[i][j] == 'N':
                flag = False
                print(f"{arr[i - j % n][0]} was nasty about {name}")
    if flag:
        print("Nobody was nasty")


def main():
    idx = 1
    while 1:
        n = int(input())
        if n == 0:
            break

        if idx != 1:
            print()
        print(f"Group {idx}")
        arr = [list(input().split()) for _ in range(n)]
        solve(n, arr)
        idx += 1


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
