import sys

def main():
    a = int(input())
    b = int(input())
    print(max(0, a * 8 + b * 3 - 28))


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
