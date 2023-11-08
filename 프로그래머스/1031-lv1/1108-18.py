#문자열 나누기
def solution(s):
    answer = 0
    left=0
    right=0
    for x in s:
        if left == right:
            answer+=1
            temp = x
        if temp == x:
            left+=1
        else:
            right+=1
    return answer