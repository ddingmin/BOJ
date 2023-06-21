import sys
input = sys.stdin.readline


def val(msg):
    visit = [0] * 26
    for i in range(len(msg)):
        idx = ord(msg[i]) - ord('A')
        visit[idx] += 1
        if visit[idx] == 3:
            visit[idx] = -1
            if i + 1 >= len(msg):
                return "FAKE"
            if msg[i] != msg[i + 1]:
                return "FAKE"
    return "OK"


for _ in range(int(input())):
    msg = input().strip()
    print(val(msg))