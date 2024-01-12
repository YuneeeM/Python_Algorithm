# [PCCP 모의고사 #1] 2번 - 체육대회
from itertools import permutations
answer = 0


def DFS(cnt, s, ability, visit):
    global answer

    std = len(ability)  # 학생수
    pro = len(ability[0])  # 종목수

    # 끝나는 조건
    if cnt == pro:
        answer = max(answer, s)

    else:
        for i in range(std):
            if visit[i] == 0:  # 이 학생을 운동에 보낸 적이 없다면?
                visit[i] = 1  # 학생 사용
                DFS(cnt+1, s+ability[i][cnt], ability, visit)
                visit[i] = 0  # 백트래킹(방문자의 취소)


def solution(ability):

    visit = [0 for i in range(len(ability))]

    # 종목수카운트, 능력치 합, 능력치들, 방문처리
    DFS(0, 0, ability, visit)

    return answer


print("-----------------------------------------------------")


def solution2(ability):
    answer = 0

    nPr = list(permutations(ability, len(ability[0])))
    for i in range(len(nPr)):
        total = 0
        for j in range(len(nPr[i])):
            total += nPr[i][j][j]
        answer = max(answer, total)
    return answer
