import sys
from itertools import combinations as cb
from itertools import permutations as pm
from collections import deque

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())

group = {}
member = {}
members = {}

for _ in range(n):
    gr = input().strip()
    size = int(input())
    members[gr] = []
    for _ in range(size):
        mem = input().strip()
        member[mem] = gr
        group[gr] = mem
        members[gr].append(mem)

for _ in range(m):
    name = input().strip()
    cmd = int(input())
    if cmd == 0:
        for p in sorted(members[name]):
            print(p)
    else:
        print(member[name])




