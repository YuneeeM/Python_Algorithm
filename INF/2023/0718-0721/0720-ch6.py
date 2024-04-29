import sys
import random as r
sys.stdin = open("0718/input6.txt", "rt")  # 파일 읽어오기

'''
씨름선수(그리디)

n명이 지원함
각 지원자의 키와 몸무게 정보를 알고 있음
"다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자만 뽑기로함"
만약 a라는 지원자보다 키도 몸무게도 무거운 지원자 존재 a지원자 탈락

키를 내림차순으로 정리하고 몸무게만 비교하면 됨
'''

n = int(input())

body = []

for i in range(n):
    h, w = map(int, input().split())
    body.append((h, w))

body.sort(reverse=True)

largest = 0
cnt = 0

for h, w in body:
    if largest < w:
        largest = w
        cnt += 1

print(cnt)
