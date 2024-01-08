# 완주하지 못한 선수
def solution(participant, completion):
    answer = ''
    dict = {}
    for p in participant:
        dict[p] = dict.get(p, 0) + 1
    for c in completion:
        dict[c] -= 1

    for key, value in dict.items():
        if value > 0:
            answer += key

    return answer


def solution2(participant, completion):
    answer = ''
    # del 딕셔너리[키] <--- 키 삭제(변수 삭제 명령어 del)
    # 참가자 명단 : 각 이름별로 몇명
    # 완주인원을 각각 참가자 명단에서 1명씩 제외
    # 마지막 1명이 남은 자가 미완주자

    # 참가자 이름마다의 인원수
    part = {}
    for i in participant:
        if i in part:
            part[i] += 1  # 있다면 추가 1명
        else:
            part[i] = 1  # 없다면 새로운 인원 1명

    # 완주인원 모두를 한명씩 빼주는 반복
    for i in completion:
        if part[i] == 1:
            del part[i]

        else:  # 한명이 아니면 한명 감소
            part[i] -= 1

    # part에는 1명만 남음
    list(part)
    return answer[0]


def solution3(participant, completion):
    answer = ''
    # 둘다 정렬
    participant.sort()
    completion.sort()
    # 일대일 비교
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    # 일대일 비교가 모두 넘어가면 마지막 주자
    return participant[-1]
