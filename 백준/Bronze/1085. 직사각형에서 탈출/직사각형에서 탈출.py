x, y, w, h = map(int, input().split())

print(min(abs(w - x), abs(h - y), abs(0 - x), abs(0 - y)))