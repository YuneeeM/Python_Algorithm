# 자연수 뒤집어 배열로 만들기
def solution1(n):
    answer = [int(x) for x in str(n)]

    return answer[::-1]


def solution2(n):
    answer = []
    # 1번 방법 : 연산식을 사용해서 (//)
    n = 12345
    while n > 0:
        answer.append(n % 10)
        n //= 10
    return answer


def solution3(n):

    return list(map(int, str(n)))[:: -1]
