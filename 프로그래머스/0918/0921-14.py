# 외계행성의 나이
def solution(age):
    answer = ''
    arr = []
    for i in str(age):
        arr.append(i)
    for x in arr:
        answer += chr(int(x)+97)
    return answer
