import sys
from collections import deque
sys.stdin = open("0801/input5.txt", "rt")  # 파일 읽어오기

'''
공주 구하기 ( 큐 자료구조로 해결) FIFO 선입선출

왕자 n명 공주하나 구하러 감
1~n 나이순 숫자 -> 시계방향으로 돌아가면 동그랗게 앉음
1번 부터 돌아가면서 번호를 외침, 한 왕자가 X 특정 숫자를 외치면 그 왕자는 공주를 구하러 가는데서 제외됨
원밖으로 나옴
'''
n, x = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)

while dq:
    for _ in range(x-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()
