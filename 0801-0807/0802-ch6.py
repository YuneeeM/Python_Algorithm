import sys
from collections import deque

sys.stdin = open("0801/input6.txt", "rt")  # 파일 읽어오기

'''
응급실

메디컬 병원 응급실에는 의사가 한 명 밖에 없습니다.
응급실은 환자가 도착한 순서대로 진료함
하지만 위험도 높으면 먼저함

환자가 접수한 대로 목록에서 제일 앞에서 환자목록을 꺼냄 popleft()
나머지 대기 목록에서 꺼낸 환자 보다 위험도가 높은 환자가 존재하면 대기 목록 제일 뒤로 다시 넣음


'''

n, m = map(int, input().split())

dq = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
dq = deque(dq)
cnt = 0

while True:
    cur = dq.popleft()
    if any(cur[1] < x[1] for x in dq):
        dq.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break
print(cnt)
