input = __import__('sys').stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def binary_search(find):
    # find 보다 작은 값을 찾아야함.
    low, high = 0, len(lis)
    while low < high:
        mid = low + (high - low) // 2

        if lis[mid] < find:
            low = mid + 1
        else:
            high = mid
    # print(lis, lis[mid], find)
    return low

lis = []
for i in arr:
    if not lis:
        lis.append(i)
    else:
        if lis[-1] < i:
            lis.append(i)
        else:
            # 이분탐색으로 대치할 값 찾기
            idx = binary_search(i)
            lis[idx] = i
print(len(lis))