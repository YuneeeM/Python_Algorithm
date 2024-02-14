#네트워크
def solution(n, computers):
    answer = 0
    visit = [0 for i in range(n)]
    for i in range(n):
        if visit[i] == 0:
            bfs(n,computers,i,visit)
            answer+=1
    return answer

def bfs(n,computers,i,visit):
    visit[i] = 1
    q =[]
    q.append(i)
    while len(q) != 0:
        i = q.pop(0)
        visit[i] = 1
        for k in range(n):
            if k != i and computers[i][k] == 1:
                if visit[k] == 0:
                    q.append(k)