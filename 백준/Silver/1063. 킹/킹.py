move = {
    "R": (0, 1),
    "L": (0, -1),
    "B": (1, 0),
    'T': (-1, 0),
    'RT': (-1, 1),
    'LT': (-1, -1),
    'RB': (1, 1),
    'LB': (1, -1)
}

def solve(king, stone, moves):
    for m in moves:
        i, j = king
        dx, dy = move[m]
        x, y = i + dx, j + dy
        if not(0 <= x < 8 and 0 <= y < 8): continue
        elif (x, y) == stone:
            s_x, s_y = stone[0] + dx, stone[1] + dy
            if not(0 <= s_x < 8 and 0 <= s_y < 8): continue
            stone = (s_x, s_y)
            king = (x, y)
        else:
            king = (x, y)
    
    return king, stone

# input
king, stone, n = input().split()
king = (8 - int(king[1]), ord(king[0]) - ord('A'))
stone = (8 - int(stone[1]), ord(stone[0]) - ord('A'))

moves = []
for _ in range(int(n)):
    moves.append(input().strip())

king, stone = solve(king, stone, moves)
print(chr(king[1] + ord('A')) + str(8 - king[0]))
print(chr(stone[1] + ord('A')) + str(8 - stone[0]))
