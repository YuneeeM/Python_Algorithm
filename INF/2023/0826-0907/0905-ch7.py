import sys
from collections import deque
sys.stdin = open("0826/input7.txt", "rt")  # 파일 읽어오기
sys.setrecursionlimit(10**6)

'''
가장 높은 탑 쌓기

밑면이 정사각형인 직육면체 벽돌들을 사용하여 탑을 쌓고자 함

(조건1) 벽돌은 회전시킬 수 없다. 즉, 옆면을 밑면으로 사용할 수 없다.
(조건2) 밑면의 넓이가 같은 벽돌은 없으며, 또한 무게가 같은 벽돌도 없다.
(조건3) 벽돌들의 높이는 같을 수도 있다.
(조건4) 탑을 쌓을 때 밑면이 좁은 벽돌 위에 밑면이 넓은 벽돌은 놓을 수 없다.
(조건5) 무게가 무거운 벽돌을 무게가 가벼운 벽돌 위에 놓을 수 없다.
'''

n = int(input())
arr = []
for i in range(n):
    m, h, w = map(int, input().split())
    arr.append((m, h, w))
arr.sort(reverse=True)
dy = [0]*n
dy[0] = arr[0][1]
res = arr[0][1]
for i in range(1, n):
    result_height = 0
    for j in range(i-1, -1, -1):
        if arr[j][2] > arr[i][2] and dy[j] > result_height:
            result_height = dy[j]
    dy[i] = result_height+arr[i][1]
    res = max(res, dy[i])
print(res)
