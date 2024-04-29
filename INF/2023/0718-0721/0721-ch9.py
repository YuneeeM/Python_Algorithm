import sys
import random as r
sys.stdin = open("0718/input9.txt", "rt")  # 파일 읽어오기

'''
증가수열 만들기(그리디)

1~n까지의 모든 자연수로 구성된 길이 n의 수열이 주어짐

'''
n = int(input())

a = list(map(int, input().split()))

lt = 0
rt = n-1
last = 0

res = ""
tmp = []

while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res = res+tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()

print(len(res))
print(res)
