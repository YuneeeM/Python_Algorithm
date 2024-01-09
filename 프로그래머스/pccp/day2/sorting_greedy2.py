# 예산
def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
        else:
            break
    return answer


def solution2(d, budget):
    answer = 0
    # 각 부서에 필요한 금액 오름차순 정렬
    d.sort()

    # 가지고 있는 금액에서 부서마다 차감
    for i in d:
        # 가지고 있는 금액으로 부서에 지원할 수 있는가?
        if budget >= i:
            budget -= i
            answer += 1
        else:  # 지원할 수 없다면?
            break
