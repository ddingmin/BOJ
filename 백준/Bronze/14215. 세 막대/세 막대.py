length = sorted(list(map(int, input().split())))

if length[0] + length[1] > length[2]:
    print(sum(length))
else:
    print(sum(length) + (length[0] + length[1] - length[2] - 1))
    