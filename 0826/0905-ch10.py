import sys
from collections import deque
sys.stdin = open("0826/input10.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)

'''
가방 문제(냅색 알고리즘)

최고 17kg의 무게를 저장할 수 있는 가방이 있음
그리고 각각 3kg, 4kg, 7kg, 8kg, 9kg의 무게를 가진 5종류의 보석이 있다.
이 보석들의 가치는 각각 4, 5, 10, 11, 13이다.
이 보석을 가방에 담는데 17kg를 넘지 않으면서 최대의 가치가 되도록 하려면 어떻게 담아야 
할까요? 각 종류별 보석의 개수는 무한이 많다. 한 종류의 보석을 여러 번 가방에 담을 수 있
다는 뜻입니다.
'''

n, m = map(int, input().split())
dy = [0]*(m+1)
for i in range(n):
    w, v = map(int, input().split())
    for j in range(w, m+1):
        dy[j] = max(dy[j], dy[j-w]+v)
print(dy[m])
