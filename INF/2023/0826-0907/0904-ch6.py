import sys
from collections import deque
sys.stdin = open("0826/input6.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)

'''
최대 선 연결하기
왼쪽의 번호와 오른쪽의 번호가 있는 그림에서 같은 번호끼리 선으로 연결하려고 함
왼쪽번호는 무조건 위에서부터 차례로 1부터 n까지 오름차순으로 나열됨

'''

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
res = 0
dy = [0]*(n+1)
dy[1] = 1
for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]
    dy[i] = max+1
    if dy[i] > res:
        res = dy[i]
print(res)
