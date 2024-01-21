import sys
import math


def solve(word):
    size = int(math.sqrt(len(word)))
    arr = []

    for i in range(size):
        arr.append(word[i * size:  i * size + size])

    arr = list(zip(*arr[::-1]))
    arr = list(zip(*arr[::-1]))
    arr = list(zip(*arr[::-1]))

    for pp in arr:
        print("".join(map(str, pp)), end = "")
    print()


def main():
    n = int(input())
    for _ in range(n):
        word = input().strip()
        solve(word)


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
