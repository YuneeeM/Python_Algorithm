import sys
import random as r
sys.stdin = open("0715/input6.txt", "rt")  # 파일 읽어오기

'''
격자판 최대합
n*n의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합을 출력함
'''

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

largest = -2147000000

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

print(largest)
