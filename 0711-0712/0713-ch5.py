import sys
import random as r
sys.stdin = open("0711-0712/input3.txt", "rt")  # 파일 읽어오기

'''
정다면체
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램을 작성해라
정답이 여러 개일 경우 오름차순으로 출력

첫번째 줄에 n m 입력받음

cnt 리스트를 만들어 해당 주사위 합계 출력값을 증가시킴
'''

n, m = map(int, input().split())

cnt = [0]*(n+m+3)

for i in range(1, n+1):
    for j in range(1, m+1):
        sum = i+j
        cnt[sum] += 1

max = -214700000

for i in range(n+m+1):
    if (cnt[i] > max):
        max = cnt[i]

for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=" ")


# n, m = map(int, input().split())
# sum = []
# dup = []
# count = 0
# value = []
# value_ = ""

# max = -1

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         sum.append(i+j)

# sum.sort()

# for i in range(0, n*m-1):
#     if sum[i] == sum[i+1]:
#         count += 1
#         value_ = sum[i]
#     else:
#         dup.append(count)
#         value.append(value_)
#         count = 0
#         value_ = ""


# for i in range(len(dup)):
#     if (dup[i] > max):
#         max = i
#     elif (dup[i] == max):
#         print(value[i], end=' ')
