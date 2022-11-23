input = __import__('sys').stdin.readline

n = int(input())

arr = sorted(list(map(int, input().split())))

total = 1
for next in arr:
    if total < next:
        print(total)
        exit(0)
    else:
        total += next

print(total)