from collections import deque

input = __import__('sys').stdin.readline
t = int(input())


for _ in range(t):
    p = list(input().strip())
    n = int(input())
    arr = input().strip()
    if arr == '[]': arr = []
    else: arr = deque(map(int,arr[1:-1].split(',')))
    err = False
    rev = 0
    for i in p:
        if i == 'R':
            rev += 1
        elif i == 'D':
            if len(arr) == 0:
                err = True
                break
            else:
                if rev % 2 == 0: arr.popleft()
                else: arr.pop()
    if err: print('error')
    else:
        if rev % 2 == 1: arr.reverse() 
        print('['+",".join(map(str,arr))+']')
