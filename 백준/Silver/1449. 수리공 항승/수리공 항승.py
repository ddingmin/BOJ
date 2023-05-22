import sys

input = sys.stdin.readline
######################### solve ###############################


def solve():
    n, l = map(int, input().split())
    nums = sorted(list(map(int, input().split())))

    start = None
    answer = 0
    for i in nums:
        if start == None:
            start = i
            answer += 1
        else:
            if start <= i and i < start + l:
                continue
            else:
                start = i
                answer += 1

    print(answer)


###############################################################

solve()
