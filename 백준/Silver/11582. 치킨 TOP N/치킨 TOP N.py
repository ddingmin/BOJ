n = int(input())
arr = list(map(int, input().split()))
k = int(input())
ans = []
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    if len(low_arr) == n // k:
        ans.append(low_arr + high_arr)
    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    #print(merged_arr)
    return merged_arr

def solve(arr):
    return merge_sort(arr)

temp = solve(arr)
if ans:
    for p in ans:
        print(*p, end = " ")
else:
    print(*temp)