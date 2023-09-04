import sys
from collections import deque
sys.stdin = open("0826/input5.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)
'''
최대 부분 증가 수열
n개의 자연수로 이루어진 수열이 주어졌을 때, 그 중에서 가장 길게 증가하는(작은 수에서 큰 수로)
원소들의 집합을 찾는 프로그램
예를 들어, 원소가 2, 7, 5, 8, 6, 4, 7, 
12, 3 이면 가장 길게 증가하도록 원소들을 차례대로 뽑아내면 2, 5, 6, 7, 12를 뽑아내어 길
이가 5인 최대 부분 증가수열을 만들 수 있다.
'''

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0]*(n+1)
dy[1] = 1
res = 0

for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]
    dy[i] = max+1
    if dy[i] > res:
        res = dy[i]
print(res)
