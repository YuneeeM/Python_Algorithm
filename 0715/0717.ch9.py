import sys
import random as r
sys.stdin = open("0715/input9.txt", "rt")  # 파일 읽어오기

'''
봉우리
지도정보 n*n격자판

'''

# 위오른쪽아래왼쪽 (시계방향)
dx = [-1, 0, 1, 0]  # 마공일공
dy = [0, 1, 0, -1]  # 공일공마

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n)  # 첫 행에 [0]*n개 추가
a.append([0]*n)  # 마지막행에 [0]*n개 추가

for x in a:
    x.insert(0, 0)  # 첫 열에 0추가
    x.append(0)  # 마지막열에 0추가

cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
