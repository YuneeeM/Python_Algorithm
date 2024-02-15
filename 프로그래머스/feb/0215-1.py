# 단어 변환
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    return bfs(begin,target,words)

#최소 단계를 찾아야 하므로 bfs
def bfs(begin,target,words):
    q = deque()
    #시작 단어와 단계 0으로 초기화
    q.append((begin,0))
    
    while q:
        now, step = q.popleft()
        
        if now == target:
            return step
        
        #단어를 모두 체크하면서, 해당 단어가 변경될 수 있는지 체크
        for word in words:
            cnt = 0
            #단어의 길이만큼 반복하여
            for i in range(len(now)):
                #단어에 알파벳 한개씩 체크하기
                if now[i] != word[i]:
                    cnt+=1
            if cnt == 1:
                q.append((word,step+1))