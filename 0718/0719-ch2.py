import sys
import random as r
sys.stdin = open("0718/input2.txt", "rt")  # 파일 읽어오기


'''
랜섬자르기(결정알고리즘)☆☆

-결정알고리즘의 특징
특정 범위안에 있다는 것을 알 수 있음
중앙값을 딱 정하고, 이 값이 유효한 지 확인할 때 이분 검색 활용
범위를 좁혀 절반은 날리고 비교해서 계산함

k개의 랜선을 가짐, 그러나 k개의 랜선은 길이가 제각각임
선생님이 랜선을 모두 n개의 같은 길이의 랜선으로 만들고 싶었기 때문에 k개의 랜선을 잘라서 만들어야 함
ex) 300cm 짜리 랜선을 140cm *2 = > 20cm는 버려야 함

'''


def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x//len)
    return cnt


k, n = map(int, input().split())
Line = []
res = 0
largest = 0


for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest

while lt <= rt:
    mid = (lt+rt)//2
    if Count(mid) >= n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1

print(res)
