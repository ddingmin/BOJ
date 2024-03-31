def solve(a, b, c, d):
    return a * 56 + b * 24 + c * 14 + 6 * d


a, b, c, d = map(int, input().split())

print(solve(a, b, c, d))
