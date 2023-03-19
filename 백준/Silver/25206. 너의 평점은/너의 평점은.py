import sys

input = sys.stdin.readline

total = 0
count = 0
for _ in range(20):
    a, b, c = input().split()
    b = int(float(b))
    if c == 'P': continue
    elif c == 'A+':
        total += 4.5 * b
    elif c == 'A0':
        total += 4 * b
    elif c == 'B+':
        total += 3.5 * b
    elif c == 'B0':
        total += 3 * b
    elif c == 'C+':
        total += 2.5 * b
    elif c == 'C0':
        total += 2 * b
    elif c == 'D+':
        total += 1.5 * b
    elif c == 'D0':
        total += 1 * b
    
    count += b

print(total / count)