# 자연수 뒤집어 배열로 만들기
def solution(n):
    answer = []
    n = [x for x in str(n)]
    for x in range(-1, -(len(n))-1, -1):
        answer.append(int(n[x]))
    return answer
