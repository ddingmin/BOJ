# input
input = __import__('sys').stdin.readline

n = int(input())

def solve():
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    arr = sorted(arr)
    for k in arr:
        print(k)
solve()