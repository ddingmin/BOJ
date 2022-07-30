input = __import__('sys').stdin.readline
n = int(input())
arr = [0] * 30
for _ in range(n):
    s = input().strip()
    s = s[::-1]
    for i in range(len(s)):
        al = s[i]
        arr[(ord(al)-ord('A'))] += 10 ** i
arr = sorted(arr, reverse = True)
cnt = 9
for i in range(10):
    arr[i] *= cnt
    cnt -= 1
print(sum(arr))