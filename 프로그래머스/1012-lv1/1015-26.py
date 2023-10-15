# 부족한 금액 계산하기
def solution(price, money, count):
    answer = 0

    for i in range(price, price*count+1, price):
        answer += i

    answer = answer-money
    if answer < 0:
        return 0
    return answer
