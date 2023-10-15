# 최대공약수와 최소공배수
def solution(n, m):
    answer = []
    res = []
    for i in range(1, min(n, m)+1):
        if n % i == 0 and m % i == 0:
            res.append(i)

    for i in range(max(n, m), (n*m)+1):
        if i % n == 0 and i % m == 0:
            min_val = i
            break
    max_val = max(res)
    answer.append(max_val)
    answer.append(min_val)
    return answer
