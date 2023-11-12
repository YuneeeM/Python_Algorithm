#실패율
def solution(N, stages):
    failure_rates = []  # (스테이지 번호, 실패율) 튜플을 저장할 리스트

    total_players = len(stages)  # 전체 플레이어 수

    for stage in range(1, N + 1):
        if total_players == 0:
            failure_rate = 0  # 스테이지에 도달한 플레이어가 없을 경우 실패율 0
        else:
            players_on_stage = stages.count(stage)  # 스테이지에 도달한 플레이어 수
            failure_rate = players_on_stage / total_players  # 실패율 계산
            total_players -= players_on_stage

        failure_rates.append((stage, failure_rate))

    # 실패율을 기준으로 정렬
    failure_rates.sort(key=lambda x: x[1], reverse=True)

    # 스테이지 번호만 추출
    answer = [stage for stage, _ in failure_rates]

    return answer
