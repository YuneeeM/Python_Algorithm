import sys
from collections import deque
sys.stdin = open("0826/input3.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)  # 백준에서 채점할때 사용해야함!(재귀 시 데이터가 많을 경우)
'''
도전과제 : 돌다리 건너기 (Bottom-Up)
철수는 학교에 가는데 개울을 만났습니다. 개울은 N개의 돌로 다리를 만들어 놓았습니다. 철
수는 돌 다리를 건널 때 한 번에 한 칸 또는 두 칸씩 건너뛰면서 돌다리를 건널 수 있습니다. 
철수가 개울을 건너는 방법은 몇 가지일까요?
'''


n = int(input())
dy = [0]*(n+2)
dy[1] = 1
dy[2] = 2
for i in range(3, n+2):
    dy[i] = dy[i-1]+dy[i-2]

print(dy[n+1])
