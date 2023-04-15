dir = {"W": (0, -1), 'E': (0, 1), 'N': (-1, 0), 'S': (1, 0)}
def solution(park, routes):
    n, m = len(park), len(park[0])
    def move(i, j, d, dist):
        start = [i, j]
        for _ in range(dist):
            x, y = i + dir[d][0], j + dir[d][1]
            if not(0 <= x < n and 0 <= y < m):
                return start
            if park[x][y] == 'X':
                return start
            i, j = x, y
        return i, j
            
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                start = [i, j]
                
    for do in range(len(routes)):
        i, j = start
        d, dist = routes[do].split()
        dist = int(dist)
        start = move(i, j, d ,dist)
    
    return start