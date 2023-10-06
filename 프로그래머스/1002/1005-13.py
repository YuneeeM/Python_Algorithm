# 저주의 숫자 3
def solution(n):
    answer = 0
    for x in range(1, n+1):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer
