number = 0
answer = -1
def z(size, x, y, r, c):
    global answer
    global number

    max_size = 2 ** (size - 1)
    if size > 1:
        if (x <= r < x + max_size) and (y <= c < y + max_size):
            z(size - 1, x, y, r, c)
        else:
            number += 4 ** (size - 1)

        if (x <= r < x + max_size) and (y + max_size <= c < y + 2 * (max_size)):
            z(size - 1, x, y + max_size, r, c)
        else:
            number += 4 ** (size - 1)

        if (x + max_size <= r < x + 2 * (max_size)) and (y <= c < y + max_size):
            z(size - 1, x + max_size, y, r, c)
        else:
            number += 4 ** (size - 1)
        if (x + max_size <= r < x + 2 * (max_size)) and (y + max_size <= c < y + 2 * (max_size)):
            z(size - 1, x + max_size, y + max_size, r, c)
        else:
            number += 4 ** (size - 1)
        
    else:
        if (x, y) == (r, c):
            answer = number
        elif (x, y + 1) == (r, c):
            answer = number + 1
        elif (x + 1, y) == (r, c):
            answer = number + 2
        elif (x + 1, y + 1) == (r, c):
            answer = number + 3
        number += 4

def solve(size, r, c):
    z(size, 0, 0, r, c)
    return answer

N, r, c = map(int, input().split())
print(solve(N, r, c))
