a, b, c = map(int, input().split())

def game(a, b, c):
    if a == b == c:
        return "*"
    if a != b and a != c:
        return "A"
    if b != a and b != c:
        return "B"
    if c != a and c != b:
        return "C"

print(game(a, b, c))