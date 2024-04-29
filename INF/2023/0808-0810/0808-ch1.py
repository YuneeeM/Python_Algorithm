import sys
from collections import deque

sys.stdin = open("0808/input1.txt", "rt")  # 파일 읽어오기

'''
재귀함수를 이용한 이진수 출력

10진수 n이 입력되면 2진수로 변환하여 출력하는 프로그램
재귀함수를 이용해야함

'''


def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x % 2, end='')


if __name__ == "__main__":
    n = int(input())
    DFS(n)
