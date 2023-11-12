# 배열 뒤집기

def solution(num_list):
    answer = []
    n = len(num_list)
    n = n+1
    print(n)
    i = -1
    for i in range(-1, -n, -1):
        cur = num_list[i]
        answer.append(cur)
    return answer
