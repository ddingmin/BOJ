import sys


def solve(word):
    ans = set()

    for i in range(1, len(word)):
        one = word[:i]
        for j in range(i + 1, len(word)):
            two = word[i:j]
            three = word[j:]
            ans.add(one[::-1] + two[::-1] + three[::-1])

    return sorted(ans)[0]


def main():
    word = input().strip()
    print(solve(word))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
