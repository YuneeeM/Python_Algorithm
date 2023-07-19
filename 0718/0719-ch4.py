import sys
import random as r
sys.stdin = open("0718/input4.txt", "rt")  # 파일 읽어오기

'''
마구간 정하기(결정 알고리즘)
n개의 마구간이 수직선상에 있음
현수는 c마리의 말을 가짐, 이 말들은 서로 가까이 있는 것을 좋아하지 않음
각 마구간에는 한 마리의 말만 넣을 수 있음, 가장 가까운 두 말의 거리가 최대가 되게 말을
마구간에 배치하고 싶음
c마리의 말을 n개의 마구간에 배치했을 때 가장 가까운 두 말의 거리가 최대가 되는 그 최대값을 출력하는 프로그램
'''


def Count(len):
    cnt = 1
    ep = Line[0]
    for i in range(1, n):
        if Line[i]-ep >= len:
            cnt += 1
            ep = Line[i]
    return cnt


n, c = map(int, input().split())
Line = []

for _ in range(n):
    tmp = int(input())
    Line.append(tmp)

Line.sort()

lt = 1
rt = Line[n-1]

res = 0

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)
