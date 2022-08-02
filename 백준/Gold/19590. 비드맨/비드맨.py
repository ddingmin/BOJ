input = __import__('sys').stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
_max = max(arr)
_sum = sum(arr)

# n == 1: 부딪힐 구슬이 없어 그냥 답
if n == 1: print(arr[0])
else:
    # 가장 많은 구슬이 다른 종류의 구슬들보다 큰 경우 다른 종류의 구슬들이 모두 가장 큰 구슬에 부딪혀 없애고 남은 값이 답
    if _max >= _sum - _max: print(_max - (_sum - _max))
    # 아닌 경우 구슬의 총 합이 홀수면 1 아니면 0
    else:
        if _sum % 2: print(1)
        else: print(0)
