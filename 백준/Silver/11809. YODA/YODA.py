import sys


def solve(a, b):
    ans = [[] for _ in range(2)]
    if len(a) > len(b):
        b = [0] * (len(a) - len(b)) + b
    else:
        a = [0] * (len(b) - len(a)) + a
    for i in range(max(len(a), len(b))):
        if not (i < len(a)):
            ans[1].append(b[i])
        elif not (i < len(b)):
            ans[0].append(a[i])
        else:
            if a[i] > b[i]:
                ans[0].append(a[i])
            elif a[i] < b[i]:
                ans[1].append(b[i])
            else:
                ans[0].append(a[i])
                ans[1].append(b[i])
    if not ans[0]:
        print("YODA")
        print(int("".join(map(str, ans[1]))))
    elif not ans[1]:
        print(int("".join(map(str, ans[0]))))
        print("YODA")
    else:
        print(int("".join(map(str, ans[0]))))
        print(int("".join(map(str, ans[1]))))


def main():
    a = list(map(int, list(input().strip())))
    b = list(map(int, list(input().strip())))
    solve(a, b)


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
