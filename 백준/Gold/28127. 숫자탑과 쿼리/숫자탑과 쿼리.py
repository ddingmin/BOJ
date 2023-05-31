import sys
input = sys.stdin.readline

q = int(input())
for step in range(q):
    a, d, x = map(int, input().split())
    
    level = 1
    _max = a
    _min = 1
    
    # print("step:", step + 1)
    while not(_min <= x <= _max):
        # print(_min, _max)
        _min = _max + 1
        _max = _min + a + (level * d) - 1
        level += 1
    print(level, x - _min + 1)
        