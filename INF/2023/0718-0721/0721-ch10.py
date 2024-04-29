import sys
import random as r
sys.stdin = open("0718/input10.txt", "rt")  # 파일 읽어오기

'''
역수열(그리디)

1~n까지의 수를 한번씩만 사용하여 이루어진 수열이 있을때, 
1부터 n까지 각각의 수 앞에 놓여 있는 자신보다 큰 수들의 개수를 수열로 표현한 것을 역수열이라함
'''

# n = int(input())
# a = list(map(int, input().split()))
# seq = [0]*n

# for i in range(n):
#     for j in range(n):
#         if a[i] == 0 and seq[j] == 0:
#             seq[j] = i+1
#             break
#         elif seq[j] == 0:
#             a[i] -= 1

# for x in seq:
#     print(x, end=" ")

n = int(input())
a = list(map(int, input().split()))
seq = [0]*n

for i in range(n):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break
        elif seq[j] == 0:
            a[i] -= 1

for x in seq:
    print(x, end=" ")
