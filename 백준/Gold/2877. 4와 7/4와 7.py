import sys
import math
input = sys.stdin.readline

k = int(input())

def solve(k):
    target = int(math.log2(k + 1))
    for i in range(1, target):
        k -= 2 ** i
    k -= 1
    return bin(k)[2:].replace('0', '4').replace('1', '7').rjust(target, '4')
print(solve(k))