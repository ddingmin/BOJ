input = __import__('sys').stdin.readline

n, k, a, b = map(int, input().split())

def solve():
    arr = [k] * n
    idx = 0
    day = 1
    while 1:
        # A개 만큼 물주기
        for _ in range(a):
            arr[idx] += b
            idx += 1
            if idx == n: idx = 0
        
        # 수분 1씩 날라가기
        for i in range(n):
            arr[i] -= 1
            if arr[i] == 0: return day
        day += 1

print(solve())