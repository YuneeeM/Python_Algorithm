import sys
import random as r
sys.stdin = open("0715/input11.txt", "rt")  # 파일 읽어오기

'''
격자판 회문수

1~9까지 자연수로 채워진 7*7 격자판이 주어지면 위에서 가로방향또는 세로방향으로 길이 5자리 
회문수가 몇개 있는지 구함
회문수 121처럼 같이 앞에서 부터 읽으나 뒤에서 읽으나 같은수

구부러진거는 안됨, 가로나 세로방향만
다섯자리 회문수(?)
'''
board = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1

print(cnt)
