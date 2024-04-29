import sys
import random as r
sys.stdin = open("0711-0712/input2.txt", "rt")  # 파일 읽어오기
'''
K번째 큰 수
현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가짐
같은 수자가 여러장 있을 수도 있음
현수는 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려함
3장을 뽑을 수 있는 모든 경우를 기록함
기록한 값 중 K번째로 큰 수를 출력하는 프로그램

10 3
13 15 34 23 45 65 33 11 26 42

'''

a, b = map(int, input().split())
c = list(map(int, input().split()))
res = set()  # 중복된 값을 막는다


for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            res.add(c[i]+c[j]+c[k])
res = list(res)
res.sort(reverse=True)
print(res[b-1])

'''
i j m
1 2 3 4 5

123
124
이렇게 되면 순차적으로 앞에 중복된 값이 없이 돌 수 있음

'''
