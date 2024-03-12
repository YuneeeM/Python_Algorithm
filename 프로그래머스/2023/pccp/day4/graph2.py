# 전력망을 둘로 나누기 - 어려움

def bfs(cut, n, graph):
    # 방문 정보를 저장
    visit = [0 for i in range(n+1)]
    # 시작 위치를 둘다 방문처리(cut)
    n = 1
    visit[cut[0]] = 1
    visit[cut[1]] = 1

    q = []
    q.append(cut[0])

    while q:
        i = q.pop(0)
        for j in graph[i]:
            if visit[j] == 0:
                n += 1
                visit[j] = n
                q.append(j)
    return n


def solution(n, wires):
    answer = n
    # 그래프 정보를 생성
    graph = [[] for i in range(n+1)]

    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)

    # 모든 위치에서 bfs
    for i in wires:
        # 끊고 싶은 위치, 개수, 그래프
        # return은 체크된 전력망 수
        cnt = bfs(i, n, graph)

        answer = min(answer, abs(cnt - (n-cnt)))

    return answer
