#JadenCase 문자열 만들기
def solution(s):
    answer = ''
    for word in s.split(' '):
        answer += word.capitalize() + ' '
    return answer[:-1]
