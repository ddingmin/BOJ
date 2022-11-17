# CA와 AB의 외적
def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

result = ccw(a, b, c)
if result == 0:     # 직선
    print(0)
elif result > 1:    # 반시계
    print(1)
else:               # 시계
    print(-1)