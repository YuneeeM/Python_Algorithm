# 이상한 문자 만들기
def solution(s):
    answer = ''
    words = s.split(' ')
    for x in words:
        for i in range(len(x)):
            if i % 2 == 0:
                answer += x[i].upper()
            else:
                answer += x[i].lower()
        answer += ' '
    return answer[0:-1]
