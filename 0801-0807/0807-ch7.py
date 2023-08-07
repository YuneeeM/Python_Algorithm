import sys
from collections import deque

sys.stdin = open("0801/input7.txt", "rt")  # 파일 읽어오기

'''
교육과정 설계

현수는 1년 과정의 수업계획을 짜야함
수업중 필수과목이 있음, 이 필수과목은 반드시 이수해야함
그 순서도 정해져 있음

'''
need = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" % (i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" % (i+1))
        else:
            print("#%d NO" % (i+1))
