# 빼빼로 데이
def solution(pepero):
    answer = list(set(pepero))

    answer.sort()

    return answer


def solution2(pepero):
    answer = []
    # 중복 제거
    pepero = set(pepero)
    # 정렬을 위해 리스트로 변경, 정렬
    pepero = list(pepero)
    pepero.sort()
    # 최종 결과값
    answer = pepero
    return answer
