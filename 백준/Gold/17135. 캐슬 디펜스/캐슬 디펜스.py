from collections import deque
from itertools import combinations as cb
import copy

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def solve(n, m, d, maps):
    def game(archers, game_maps):
        kill_count = 0
        def shoot():
            deads = []
            count = 0
            for archer in archers:
                i, j = n, archer
                q = deque()
                q.append([i, j])
                visit = [[0] * m for _ in range(n)]
                dist = 0
                while q and dist < d:
                    enemy = []
                    for _ in range(len(q)):
                        i, j = q.popleft()
                        for dir in range(4):
                            x, y = i + dx[dir], j + dy[dir]
                            if not(0 <= x < n and 0 <= y < m): continue
                            if visit[x][y] == 0:
                                if game_maps[x][y] == 1:
                                    enemy.append([x, y])
                                q.append([x, y])
                                visit[x][y] = 1
                    dist += 1
                    # 가까운 적을 발견한 경우 더 탐색 X
                    if enemy: 
                        enemy.sort(key = lambda x: [x[1]])
                        deads.append(enemy[0])
                        break
            # 찾은 적 제거
            # print(deads)
            for x, y in deads:
                if game_maps[x][y] == 1:
                    game_maps[x][y] = 0
                    count += 1
            # print("죽인 적: ", len(deads))
            return count
        
        def move_enemy():
            temp = [0] * m
            for i in range(n):
                game_maps[i], temp = temp, game_maps[i]
        
        for i in range(n):
            # print(i + 1, "번째 실행")
            # for map in game_maps:
            #     print(*map)
            # print()
            kill_count += shoot()
            move_enemy()

        return kill_count
    # 궁수는 3명
    # D이하인 적중에서 가장 가까운 적 공격 (가장 왼쪽 부터) (같은 적이 여러 궁수에게 공격당할 수 있음)
    # 궁수의 공격이 끝나면 적들은 아래로 한 칸 이동
    # 적이 성이 있는 칸으로 이동한 경우 게임에서 제외
    archer_idx = []
    for i in range(m): archer_idx.append(i)
    
    answer = 0
    # 궁수의 위치 조합
    for archers in cb(archer_idx, 3):
        answer = max(answer, game(archers, copy.deepcopy(maps)))
    
    return answer

n, m, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, m, d, maps))
