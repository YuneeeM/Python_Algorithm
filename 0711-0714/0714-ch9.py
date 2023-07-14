import sys
import random as r
sys.stdin = open("0711-0714/input7.txt", "rt")  # 파일 읽어오기

'''
주사위 게임
1에서 6까지 눈을 가진 3개의 주사위 던짐
(1) 같은 눈이 3개나오면 10,000원 + (같은눈)*1,000
(2) 같은 눈이 2개 나오면 1,000 + (같은 눈)*100
(3) 모두 다름 (그중 가장 큰 값)*100
'''

# n = int(input())
# sum = [0]*n

# max = 0

# for i in range(3):
#     a, b, c = map(int, input().split())

#     if (a == b and b == c and c == a):
#         sum[i] = 10000+a*1000
#     elif (a == b or b == c or c == a):
#         if (a == b):
#             sum[i] = 1000 + a*100
#         elif (b == c):
#             sum[i] = 1000 + b*100
#         else:
#             sum[i] = 1000 + c*100
#     elif (a != b and b != c and c != a):

#         if (a > b):
#             if (a > c):
#                 max = a
#             else:
#                 max = c
#         else:
#             if (b > c):
#                 max = b
#             else:
#                 max = c
#         sum[i] = max*100

# max = 0

# for i in range(len(sum)):
#     if sum[i] > max:
#         max = sum[i]

# print(max)


n = int(input())
res = 0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        money = 10000 + a*1000
    elif a == b or a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b+100
    else:
        money = c*100
    if money > res:
        res = money
print(res)
