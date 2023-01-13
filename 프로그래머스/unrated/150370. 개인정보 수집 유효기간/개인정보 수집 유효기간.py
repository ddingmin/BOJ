def check_answer(limit_date, today):
    del_info = []
    ty, tm, td = map(int, today.split('.'))
    tm += ty * 12
    td += tm * 28
    
    for cur in limit_date:
        num, d = cur
        if td >= d: del_info.append(num)
    return del_info

def solution(today, terms, privacies):
    answer = []
    # 약관 종류 정리
    rules = {}
    for cur in terms:
        a, b = cur.split()
        rules[a] = int(b)
        
    # 파기 만료 기간 구하기
    dates = []
    for i in range(len(privacies)):
        date, r = privacies[i].split()
        y, m, d = map(int, date.split('.'))
        
        m += y * 12 + rules[r]
        d += m * 28
        dates.append([i + 1, d])
    answer = check_answer(dates, today)

    return answer