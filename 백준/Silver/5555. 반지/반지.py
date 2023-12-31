import sys


def solve(word, targets):
    ans = 0

    for target in targets:
        target += target[:-1]
        if word in target:
            ans += 1

    return ans


def main():
    word = input().strip()
    targets = []
    for _ in range(int(input())):
        targets.append(input().strip())
    print(solve(word, targets))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
