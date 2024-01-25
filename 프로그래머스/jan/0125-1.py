#점 찍기
import math
def solution(k, d):
    answer = 0
    for i in range(0,d+1,k):
        limit = math.sqrt(d**2-i**2)
        answer += limit//k + 1

    return answer

'''
완전탐색의 방법은 시간 초과가 발생함
r은 원의 반지름이 아닌 원의 반지름을 k로 나눈값이 된다
'''