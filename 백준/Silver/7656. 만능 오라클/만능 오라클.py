import sys

START = "What is"
FT = "Forty-two is"


def solve(line):
    for i in range(7, len(line)):
        if line[i - 7:i] == START:
            p = None
            for j in range(i, len(line)):
                if line[j].isupper():
                    break
                if line[j] == '?':
                    p = (FT + line[i:j] + '.')

            if p is not None:
                print(p)
    return


def main():
    line = input().strip()
    solve(line)


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
