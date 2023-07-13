import sys
import random as r
sys.stdin = open("0711-0712/input5.txt", "rt")  # 파일 읽어오기

'''
소수(에라토스테네스 체)

자연수 n이 입력되면 1부터 n까지의 소수의 개수를 출력함
만약 20이 입력되면 1부터 20까지 소수는 2,3,5,7,13,17,19로 8개 출력
'''

n = int(input())
ch = [0]*(n+1)
cnt = 0

for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)
