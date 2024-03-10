import sys


def solve(n, m, arr):
    mp = {}
    for word in arr:
        if len(word) < m:
            continue
        if word in mp:
            mp[word] += 1
        else:
            mp[word] = 1

    arr = []
    for k in mp.keys():
        arr.append([k, mp[k]])

    arr.sort(key=lambda x: [-x[1], -len(x[0]), x[0]])

    for p in arr:
        print(p[0])


def main():
    n, m = map(int, input().split())
    arr = list(input().strip() for _ in range(n))
    solve(n, m, arr)


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
