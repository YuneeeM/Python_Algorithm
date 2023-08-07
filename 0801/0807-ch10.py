import sys
import heapq as hq

sys.stdin = open("0801/input10.txt", "rt")  # 파일 읽어오기

'''
최소힙

완전 이진 트리로 구현된 자료구조
1) 자연수가 입력되면 최소힙에 입력
2) 숫자 0이 입력되면 최소힙에서 최솟값을 꺼내어 출력
(출력할 자료가 없으면 -1을 출력)
3) -1 이 입력되면 프로그램 종류

'''
a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)
