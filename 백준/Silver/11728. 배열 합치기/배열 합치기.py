n, m = input().split()
arr = list(map(int, input().split()))
arr += list(map(int, input().split()))
print(*sorted(arr))