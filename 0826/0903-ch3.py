import sys
from collections import deque
sys.stdin = open("0826/input3.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)  # 백준에서 채점할때 사용해야함!(재귀 시 데이터가 많을 경우)
'''
도전과제 : 계단오르기 (Top-Down : 메모이제이션)
철수는 계단을 오를 때 한 번에 한 계단 또는 두 계단씩 올라간다.
만약, 총 4 계단을 오른다면 그 방법의 수는 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 총 5가지
'''
