# 크기가 작은 부분문자열
def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        # 조건 : t의 p 길이 만큼 비교하는데 p보다 작으면
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer
