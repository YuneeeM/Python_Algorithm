# 순위
def solution(n, results):
    answer = 0
    graph = [[0]*n for _ in range(n)]

    # i이 j에 이겼을 때는 1로
    # i이 j에 졌을 때는 -1로
    
    for i,j in results:
        graph[i-1][j-1] = 1
        graph[j-1][i-1] = -1
        
    '''
    1. 모든 노드를 중간점(경로)로 가정하며
    2. 점수판을 순회
    3. 만약 i가 k에 이겼고, k가 j에 이겼다면
    i는 j에게도 이김 (지는 것도 동일)
    
    '''    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j or graph[i][j] in [1,-1]:
                    continue
                if graph[i][k] == graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = graph[k][i] = graph[j][k] = -1
    # 각 노드 점수판에 0이 하나 (다른 노드들에 대해 승패가 모두 결정됨)인 경우만 셈
    for row in graph:
        if row.count(0) == 1:
            answer+=1
    return answer

'''
플로이드-와샬 알고리즘
모든 노드로부터 다른 노드까지의 최단 거리를 저장하는 알고리즘
전체 알고리즘 = 삼중 반복문으로 수행됨
'''
