import sys
input = sys.stdin.readline

def solve(t, a, b):
    count = 0
    apsum, bpsum = [0], [0]
    ad, bd = {}, {}

    for i in a:
        apsum.append(apsum[-1] + i)

    for i in b:
        bpsum.append(bpsum[-1] + i)

    for i in range(len(apsum)):
        for j in range(i):
            k = apsum[i] - apsum[j]
            if k in ad:
                ad[k] += 1
            else:
                ad[k] = 1
    
    for i in range(len(bpsum)):
        for j in range(i):
            k = bpsum[i] - bpsum[j]
            if k in bd:
                bd[k] += 1
            else:
                bd[k] = 1

    for i in ad.keys():
        if t - i in bd:
            count += ad[i] * bd[t - i]

    return count

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

print(solve(t, a, b))