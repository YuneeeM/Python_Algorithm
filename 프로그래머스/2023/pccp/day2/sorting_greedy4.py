# 단속 카메라
def solution(routes):
    answer = 0

    return answer


routes = [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]

routes.sort(key=lambda x: (x[1], x[0]))
print(routes)


def solution2(routes):
    answer = 0
    # 가장 빨리 끝나는 회의 순 ...
    # 끝나는게 같다면 시작이 빠른 순
    routes.sort(key=lambda x: (x[1], x[0]))

    # 처음 회의실 사용팀 끝나는 시간 기억
    end = routes[0][1]
    # 처음 회의실 사용팀 수
    answer = 1
    # 전체팀 -1 수 만큼 비교
    for i in range(len(routes)-1):
        # 끝나는 시간보다 시작 시간이 이상입니까?
        if end < routes[i+1][0]:
            # 끝나는 시간 갱신
            end = routes[i+1][1]
            answer += 1

    return answer
