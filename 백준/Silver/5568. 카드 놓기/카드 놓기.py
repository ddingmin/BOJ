from itertools import permutations as pm

n = int(input())
k = int(input())

arr = []
for _ in range(n):
    arr.append(input())

s = set()
for i in pm(arr, k):
    s.add("".join(i))

print(len(s))