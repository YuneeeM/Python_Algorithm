# 모음 제거
def solution(my_string):
    answer = ''
    arr = ['a', 'e', 'i', 'o', 'u']
    for x in my_string:
        if x in arr:
            continue
        answer += x
    return answer
