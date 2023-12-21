import sys

MAX_VALUE = 1_000_000


def solve(n, arr):
    # 갯수 배열로 변환
    cnt = {}

    for i in arr:
        if i not in cnt:
            cnt[i] = 0
        cnt[i] += 1

    cnt_arr = []
    for i in range(n):
        cnt_arr.append([cnt[arr[i]], i])

    ans = [0] * n

    stack = []

    # 뒤에서부터 스택으로 해결
    for new, idx in cnt_arr[::-1]:
        if not stack:
            ans[idx] = -1
            stack.append([new, idx])
        elif stack and stack[-1][0] > new:
            prev, prev_idx = stack[-1]
            ans[idx] = arr[prev_idx]
            stack.append([new, idx])
        elif stack and stack[-1][0] == new:
            prev, prev_idx = stack[-1]
            ans[idx] = ans[prev_idx]
            stack.append([new, idx])
        elif stack and stack[-1][0] < new:
            while stack and stack[-1][0] < new:
                stack.pop()
            if not stack:
                ans[idx] = -1
                stack.append([new, idx])
            elif stack and stack[-1][0] > new:
                prev, prev_idx = stack[-1]
                ans[idx] = arr[prev_idx]
                stack.append([new, idx])
            elif stack and stack[-1][0] == new:
                prev, prev_idx = stack[-1]
                ans[idx] = ans[prev_idx]
                stack.append([new, idx])

    print(*ans)
    return 0


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    solve(n, arr)


if __name__ == '__main__':
    # sys.setrecursionlimit(10 ** 6)
    input = sys.stdin.readline
    main()
