# 순서쌍의 개수

def solution(n):
    answer = 0
    for i in range(1, n+1):
        for j in range(n//i, 0, -1):
            if i*j == n:
                answer += 1

    return answer
