import sys

dx, dy = [-2, -1, -1, 0, 0, 1, 1, 2], [0, -1, 1, -2, 2, -1, 1, 0]


def make(alp, ans, idx):
    draw = '#'
    if idx % 3 == 2:
        draw = '*'

    i, j = 2, 4 * idx + 2

    ans[i][j] = alp
    for k in range(8):
        x, y = i + dx[k], j + dy[k]
        if ans[x][y] == '*':
            continue
        ans[x][y] = draw


def solve(size, word):
    ans = [['.'] * (size * 5 - (size - 1)) for _ in range(5)]
    for i in range(len(word)):
        make(word[i], ans, i)

    for pp in ans:
        print("".join(map(str, pp)))


def main():
    word = input().strip()
    solve(len(word), word)


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
