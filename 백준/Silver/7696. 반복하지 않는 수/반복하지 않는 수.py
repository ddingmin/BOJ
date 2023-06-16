import sys
input = sys.stdin.readline

N = 1_000_000

mem = [0]
num = 1

def check(a):
    nums = [0] * 10
    for n in str(a):
        if nums[int(n)]:
            return False
        nums[int(n)] += 1
    return True

while len(mem) <= N:
    if check(num):
        mem.append(num)
    num += 1

while 1:
    t = int(input())
    if t == 0:
        break
    print(mem[t])