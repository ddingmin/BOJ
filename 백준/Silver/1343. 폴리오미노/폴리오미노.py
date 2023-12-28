import sys


def solve(block):
    count = 0
    for i in range(len(block)):
        if block[i] == 'X':
            count += 1

            if count == 4:
                block = block[:i - 3] + "AAAA" + block[i + 1:]
                count = 0
        else:
            if count == 2:
                block = block[:i - 2] + "BB" + block[i:]
                count = 0
            elif count == 0:
                continue
            else:
                return -1

    return block[:-1]


def main():
    block = input().strip()
    print(solve(block + "."))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
