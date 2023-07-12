import sys
import random as r
sys.stdin = open("0711-0712/input2.txt", "rt")  # 파일 읽어오기

'''
대표값 
N명의 학생 수학점수가 주어짐
N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, N명의 학생 주 평균에 가장 가까운 학생은 몇번째 학생인지 출력
평균의 가장 가까운 점수가 여러개 이면 먼저 점수가 높은 학생번호, 높은 점수를 가진 학생이 여러명일때는 그중 빠른 번호 답함

10
45 73 66 87 92 67 75 79 75 80
'''

s = int(input())
c = list(map(int, input().split()))

min = float('inf')

ave = round(sum(c)/s)  # round가 소수 첫째자리에서 반올림함

for idx, x in enumerate(c):  # enumerate에 idx는 배열의 번호, x는 값을 할당함
    tmp = abs(x-ave)  # 거리값을 절대값으로 반환(시도 좋았다)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1

print(ave, res)

'''
[74]
[73, 75, 75] 일때 elif은 만족하는데 그 안에 if문을 만족하지 않음
그래서 가장 빠른 번호를 출력하게 됨

'''
