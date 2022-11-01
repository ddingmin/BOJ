import sys

def strToint(temp):
        cnt = 0
        for i in range(len(temp)):
            cnt += int(temp[-i - 1]) * (2 ** i)
        return cnt

def intTostr(temp):
    r = "{0:b}".format(temp)
    r = str(r).zfill(8)
    return r

def solve(arr):
    pc = 0
    adder = "00000000"

    
    while 1:
        command = arr[pc]
        pc = (pc + 1) % 32
        do = command[0:3]
        
        # 타겟에는 2진수 형태 str로
        target = command[3:len(command)].zfill(8)
        
        if do == "000":     # 메모리 주소 x에 가산기의 값을 저장한다.
            arr[strToint(target)] = adder

        elif do == "001":   # 메모리 주소 x의 값을 가산기로 불러온다.
            adder = arr[strToint(target)]
                
        elif do == "010":   # 가산기의 값이 0이면 PC 값을 x로 바꾼다.
            if adder == "00000000": 
                pc = strToint(target)
        elif do == "011":   # 아무 연산도 하지 않는다
            continue
        
        elif do == "100":   # 가산기 값을 1 감소시킨다.
            adder = intTostr((strToint(adder) - 1) % 256)
        
        elif do == "101":   # 가산기 값을 1 증가시킨다.
            adder = intTostr((strToint(adder) + 1) % 256)
            
        elif do == "110":   # PC 값을 x로 바꾼다.
            pc = strToint(target)
        
        elif do == "111":
            print(adder)
            break
    
lines = sys.stdin.readlines()
arr = ["00000000"] * 32
i = 0
for line in lines:
    if line.strip() == "":
        exit(0)
    arr[i] = line.strip()
    i += 1
    if i == 32:
        solve(arr)
        arr = ["00000000"] * 32
        i = 0