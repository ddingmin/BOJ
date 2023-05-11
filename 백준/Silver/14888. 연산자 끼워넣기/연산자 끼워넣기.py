import sys
input = sys.stdin.readline

def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def multi(a, b):
    return a * b
def divide(a, b):
    if a < 0:
        a *= -1
        return -(a // b)
    return a // b

ops = [plus, minus, multi, divide]
n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

answer = [-float('inf'), float('inf')]

def bt(lef, temp):
    global answer
    
    if lef == 0:
        res = ops[temp[0]](nums[0], nums[1])
        idx = 1
        for i in range(2, len(nums)):
            res = ops[temp[idx]](res, nums[i])
            idx += 1
        answer = [max(answer[0], res), min(answer[1], res)]
        return
    
    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            temp.append(i)
            bt(lef - 1, temp)
            temp.pop()
            op[i] += 1

bt(n - 1, [])
print(answer[0])
print(answer[1])