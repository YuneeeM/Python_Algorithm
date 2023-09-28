# 한 번만 등장한 문자
def solution(s):
    answer = ''
    ch = [0]*150
    for x in s:
        ch[ord(x)] += 1

    for k, v in enumerate(ch):
        if v == 1:
            answer += chr(k)

    return answer
