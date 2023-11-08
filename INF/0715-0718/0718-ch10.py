import sys
import random as r
sys.stdin = open("0715/input10.txt", "rt")  # 파일 읽어오기


'''
스토쿠 검사
9x9크기의 보드 3x3크기의 보드가 중복없이 1~9씩
각 줄에 1~9만족
그리고 3x3에도 스토쿠가 만족해야함
'''


def check(a):
    for i in range(9):
        ch1 = [0]*10  # 행
        ch2 = [0]*10  # 열
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
    for i in range(3):
        for j in range(3):
            ch3 = [0]*10  # 그룹
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]

if check(a):
    print("YES")
else:
    print("NO")
