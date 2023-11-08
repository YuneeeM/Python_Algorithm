import sys
from collections import deque

sys.stdin = open("0801/input8.txt", "rt")  # 파일 읽어오기

'''
단어 찾기
현수는 영어로 시를 쓰는 것을 좋아함
시를 쓰기 전 시에 쓰일 단어를 미리 노트에 적어둠
n개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있음

'''

n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1

for i in range(n-1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break
