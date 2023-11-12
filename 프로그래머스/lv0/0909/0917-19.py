# 배열의 평균값
def solution(numbers):
    n = len(numbers)
    sum = 0
    for x in numbers:
        sum += x
    sum = sum/n
    return sum
