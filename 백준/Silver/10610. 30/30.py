import sys
input = sys.stdin.readline

arr = list(sorted(map(int, list(input().strip())), reverse = 1))

ans = ""

def check(arr):
    ans = ""
    flag = False
    
    temp = 0

    for num in arr:
        temp += num
        ans += str(num)
        if num == 0:
            flag = True
    
    if flag and temp % 3 == 0:
        return ans
    return -1

print(check(arr))
