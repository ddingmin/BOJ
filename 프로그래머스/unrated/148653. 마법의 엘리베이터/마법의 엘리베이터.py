def solution(storey):
    # 2가지 경우
    # 위로 올라가거나 밑으로 내려가거나
    # 올라갈 때는 다음 자릿수를 +1 해주어야 함.
    answer = []
    
    def dfs(st, count):
        if st == 0:
            answer.append(count)
            return
        
        one = st % 10
        up, down = 10 - one, one
        # up 이나 down 둘 중 더 적게 움직이는 쪽으로 이동
        if up < down:
            dfs(st // 10 + 1, count + up)
        elif down < up:
            dfs(st //10, count + down)
        else:
            # 같다면 둘다 이동해보기
            for i in range(2):
                dfs(st // 10 + i, count + up)
    
    dfs(storey, 0)
    return min(answer)