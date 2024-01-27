import sys


def solve(n, arr):
    while len(arr) > 2:
        new_arr = []
        if len(arr) % 2 == 0:
            for i in range(len(arr) // 2):
                new_arr.append(arr[i] + arr[len(arr) - i - 1])
        else:
            for i in range(len(arr) // 2):
                new_arr.append(arr[i] + arr[len(arr) - i - 1])
            new_arr.append(arr[len(arr) // 2] * 2)

        arr = new_arr

    if arr[0] > arr[1]:
        return "Alice"
    else:
        return "Bob"


def main():
    t = int(input())
    for idx in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(f"Case #{idx + 1}: {solve(n, arr)}")


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
