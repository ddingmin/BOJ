cnt = 1
while True :
    n = int(input())
    if n == 0 : break
    if n * 3 % 2 == 0 : print("{:d}. even {:d}".format(cnt, (3 * n // 2) * 3 // 9))
    else : print("{:d}. odd {:d}".format(cnt, ((3 * n + 1) // 2) * 3 // 9))
    cnt += 1

    