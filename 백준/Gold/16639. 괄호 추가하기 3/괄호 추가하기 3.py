import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*5)

n = int(input())
form = list(input().strip())
def calc(a, op, b):
    a, b = int(a), int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

answer = -1 * float('inf')

def bt(form):
    global answer
    if len(form) == 1:
        answer = max(answer, int(form[0]))
        return
    
    for i in range(1, len(form), 2):
        temp = calc(form[i - 1], form[i], form[i + 1])
        new_form = form[:i - 1] + [temp] + form[i + 2:]
        bt(new_form)

bt(form)
print(answer)