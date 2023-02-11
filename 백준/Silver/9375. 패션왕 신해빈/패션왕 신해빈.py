def solve(n, arr):
    categories = {}
    for name, category in arr:
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

    count = 1
    for c in categories:
        count *= categories[c] + 1
    count -= 1

    return count

# input
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [input().split() for _ in range(n)]
    print(solve(n, arr))