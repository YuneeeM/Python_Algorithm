import sys
from collections import deque
sys.stdin = open("0826/input12.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)

'''
최대점수 구하기(냅색 알고리즘)
이번 정보 올림피아드 대회에서 좋은 성적을 내기 위하여
현수는 선생님이 주신 n개의 문제를 풀려고 함
각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 됨
제한시간 m안에 n개의 문제 중 최대 점수를 얻을 수 있도록 해야 함
(해당 문제는 해당 시간이 걸리면 푸는 걸로 간주함, 한 유형당 한개만 풀 수 있음)
'''
n, m = map(int, input().split())
dy = [0]*(m+1)
for i in range(n):
    score, time = map(int, input().split())
    for j in range(m, time-1, -1):
        dy[j] = max(dy[j], dy[j-time]+score)
print(dy[m])
