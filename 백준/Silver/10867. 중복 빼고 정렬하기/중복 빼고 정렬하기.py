n = int(input())
nums = sorted(set(list(map(int, input().split()))))
print(*nums)