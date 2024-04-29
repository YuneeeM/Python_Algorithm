import sys
import random as r
sys.stdin = open("0718/input5.txt", "rt")  # 파일 읽어오기

'''
회의실 배정(그리디)

한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들려고 함
각 회의에 대해 시작시간과 끝나는 시간이 주어짐
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음회의가 시작됨

'''
n = int(input())

meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))
meeting.sort(key=lambda x: (x[1], x[0]))

et = 0  # 회의 끝나는 시간
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1
print(cnt)
