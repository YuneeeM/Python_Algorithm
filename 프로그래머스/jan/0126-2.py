#가장 먼 노드
def solution(n, edge):
    answer=0
    visit = [0 for _ in range(n+1)]
    graph=[[] for _ in range(n+1)]
    
    for i in range(len(edge)):
        graph[edge[i][0]].append(edge[i][1])
        graph[edge[i][1]].append(edge[i][0])
        
    visit[1] = 1
    
    q=[]
    q.append(1)
    
    while q:
        i = q.pop(0)
        for val in graph[i]:
            if visit[val] == 0:
                visit[val] = visit[i] + 1
                q.append(val)
    answer = max(visit)
    answer = visit.count(answer)
                
    return answer