# 그래프 - 가장 먼 노드
def solution(n, edge):
    answer = 0
    visit = [0 for i in range(n+1)]
    li = [[] for i in range(n+1)]

    for i in range(len(edge)):  # 3, 6
        li[edge[i][0]].append(edge[i][1])  # 3번 인덱스에 6이라는 데이터를 추가
        li[edge[i][1]].append(edge[i][0])  # 6번 인덱스에 3이라는 데이터를 추가

    # 점점 멀어지는 bfs
    q = []
    q.append(1)  # 1은 시작점
    visit[1] = 1

    # bfs
    while q:
        i = q.pop(0)
        for j in li[i]:
            # 방문한적 없다면
            if visit[j] == 0:
                visit[j] = visit[i]+1
                q.append(j)
    answer = max(visit)  # 가장 큰값(가장 멀리 떨어진 거리값)
    answer = visit.count(answer)  # 가장 큰 값이 몇개가 있는지?
    return answer
