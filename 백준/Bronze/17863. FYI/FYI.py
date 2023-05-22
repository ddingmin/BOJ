import sys

input = sys.stdin.readline
######################### solve ###############################


def solve():
    st = input().strip()[0:3]
    if st == "555":
        print("YES")
    else:
        print("NO")


###############################################################

solve()
