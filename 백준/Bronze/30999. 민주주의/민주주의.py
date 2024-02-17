import sys


def solve(n, m, visit, adj):
    pass


def main():
    n, m = map(int, input().split())
    ans = 0
    for _ in range(n):
        word = input().strip()
        cnt = 0
        for c in word:
            if c == 'O':
                cnt += 1

        if cnt > m // 2:
            ans += 1
    print(ans)



if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
