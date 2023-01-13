def hashing(date):
    y, m, d = map(int, date.split('.'))
    m += y * 12
    d += m * 28
    return d

# 약관의 종류를 딕셔너리로 정리
def get_rules(terms):
    rules = {}
    for cur in terms:
        a, b = cur.split()
        rules[a] =int(b)
    return rules

def check_answer(end_dates, today):
    target = hashing(today)
    ans = []
    for index, value in end_dates:
        if target >= value:
            ans.append(index)
    return ans
def solution(today, terms, privacies):
    answer = []
    # 약관 종류 정리
    rules = get_rules(terms)

    # 파기 만료 기간 구하기
    end_dates = []
    for i in range(len(privacies)):
        date, r = privacies[i].split()
        value = hashing(date)
        value += rules[r] * 28
        end_dates.append([i + 1, value])
    answer = check_answer(end_dates, today)

    return answer