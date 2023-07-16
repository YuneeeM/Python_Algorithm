import sys
import random as r
sys.stdin = open("0715/input5.txt", "rt")  # 파일 읽어오기

'''
수들의 합

'''

a, b = map(int, input().split())
c = list(map(int, input().split()))

lt = 0
rt = 1
tot = c[0]
cnt = 0

while True:
    if tot < b:
        if rt < a:
            tot += c[rt]
            rt += 1
        else:
            break
    elif tot == b:
        cnt += 1
        tot -= c[lt]
        lt += 1
    else:
        tot -= c[lt]
        lt += 1
print(cnt)
