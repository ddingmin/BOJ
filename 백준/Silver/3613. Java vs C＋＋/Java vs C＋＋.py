import sys
input = sys.stdin.readline

JAVA = 1
CPP = 2
ERROR = 0

line = input().strip()

def val(line):
    for i in range(1, len(line)):
        if not(line[i].isalpha() or line[i] == "_"):
            return ERROR
        
    if val_java(line) == JAVA:
        return JAVA

    if val_cpp(line) == CPP:
        return CPP
    return ERROR
        
def val_java(line):
    # 첫글자는 소문자 알파벳이야 함.
    if not (line[0].isalpha() and line[0].lower() == line[0]):
        return ERROR
    for i in range(1, len(line)):
        if not (line[i].isalpha()):
            return ERROR
    return JAVA

def val_cpp(line):
    # 첫글자 또는 마지막 글자가 _ 인경우 error
    if line[0] == "_" or line[-1] == "_":
        return ERROR
    if line[0].isalpha() and line[0].upper() == line[0]:
        return ERROR

    # 소문자랑 _ 만 가능
    for i in range(1, len(line)):
        if line[i].isalpha() and line[i].upper() == line[i]:
            return ERROR
        # __가 이어진 경우
        if line[i] == line[i - 1] == "_":
            return ERROR
    return CPP

def convert(line, code):
    temp = ""
    # JAVA to CPP
    if code == 1:
        for i in line:
            if i.upper() == i:
                temp += "_"
            temp += i.lower()
            
    # CPP to JAVA
    elif code == 2:
        flag = False
        for i in line:
            if i == "_":
                flag = True
            else:
                if flag:
                    flag = False
                    temp += i.upper()
                else:
                    temp += i
    return temp

lge = val(line)
if lge == 0:
    print("Error!")
else:
    print(convert(line, lge))