import sys
import random as r
sys.stdin = open("0718/input8.txt", "rt")  # 파일 읽어오기

'''
침몰하는 타이타닉(그리디) - queue version

유람선에는 n명의 승객이 타고 있음, 구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명이하로만 탈 수 있음, 
보트 한개에 탈 수 있는 무게도 m이하로 제한됨
'''

n, m = map(int, input().split())
person = list(map(int, input().split()))

person.sort()

cnt = 0

while person:
    if len(person) == 1:
        cnt += 1
        break
    if person[0]+person[-1] > m:
        person.pop()
        cnt += 1
    else:
        person.pop(0)
        person.pop()
        cnt += 1


print(cnt)
