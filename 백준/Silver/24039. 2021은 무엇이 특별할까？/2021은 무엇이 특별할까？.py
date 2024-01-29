import sys


def solve(n):
    prime = [1] * (20000)
    prime[0], prime[1] = 0, 0
    p = []
    for i in range(2, 20000):
        if prime[i] == 1:
            p.append(i)
            for j in range(2, 20000):
                if i * j >= 20000: break
                if prime[i * j] == 1:
                    prime[i * j] = 0

    for i in range(1, len(p)):
        if p[i] * p[i - 1] > n:
            return p[i] * p[i - 1]

    return 0


def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
