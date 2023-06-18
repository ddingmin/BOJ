import sys
input = sys.stdin.readline

# input
n = int(input())
arr = list(map(int, input().split()))

# func
def boy(a):
    num = a
    while num - 1 < n:
        arr[num - 1] ^= 1
        num += a

def girl(a):
    a -= 1
    l, r = a - 1, a + 1
    arr[a] ^= 1
    while 0 <= l and r < n:
        if arr[l] == arr[r]:
            arr[l] ^= 1
            arr[r] ^= 1
            l -= 1
            r += 1
        else:
            break

def do(a, b):
    if a == 1:
        boy(b)
    elif a == 2:
        girl(b)


# solve
for _ in range(int(input())):
    a, b = map(int, input().split())
    do(a, b)

for i in range(n):
    if i != 0 and i % 20 == 0:
        print()
    print(arr[i], end = " ")
