n, k = map(int, input().split())
data = list(map(int, input().split()))
print(sorted(data, reverse = True)[k - 1])