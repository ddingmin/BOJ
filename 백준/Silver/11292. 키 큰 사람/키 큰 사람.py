import sys


def solve(arr):
    arr.sort(key = lambda x: [-x[1]])

    _max = arr[0][1]
    ans = []
    for name, v in arr:
        if v == _max:
            ans.append(name)
    return " ".join(ans)


def main():
    while 1:
        t = int(input())
        if t == 0:
            break

        arr = []
        for _ in range(t):
            name, value = input().split()
            arr.append([name, float(value)])
        print(solve(arr))



if __name__ == '__main__':
    input = sys.stdin.readline
    main()
