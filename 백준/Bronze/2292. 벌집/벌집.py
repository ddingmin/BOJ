answer = 1
end = 1
jump = 0
n = int(input())
while 1:
    if n <= end:
        print(answer)
        exit(0)
    else:
        answer += 1
        jump += 6
        end += jump