import sys


def find_max(size, cutting):
    max_cut = 0
    prev = 0
    for i in cutting:
        max_cut = max(max_cut, i - prev)
        prev = i
    max_cut = max(max_cut, size - prev)

    return max_cut


def solve(n, m, w, h):
    return find_max(m, w) * find_max(n, h)


def main():
    n, m = map(int, input().split())
    w, h = [], []
    size = int(input())
    for _ in range(size):
        cmd, t = map(int, input().split())
        if cmd == 0:
            w.append(t)
        else:
            h.append(t)
    print(solve(n, m, sorted(w), sorted(h)))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
