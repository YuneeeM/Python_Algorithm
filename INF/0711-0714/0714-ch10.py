import sys
import random as r
sys.stdin = open("0711-0714/input8.txt", "rt")  # 파일 읽어오기

'''
점수 계산
ox 문제는 맞거나 틀린 두 경우의 답을 가지는 문제를 말함
여러개의 ox문제로 만들어진 시험에서 연속적으로 답을 맞히는 경우에 가산점줌
k번째 문제는 k점으로 계산
틀린 문제는 0점
'''

# n = int(input())
# ans = list(map(int, input().split()))

# sum = 0
# cnt = 0

# for i in range(len(ans)):
#     if ans[i] == 0:
#         sum += 0
#         cnt = 0
#     else:
#         if (ans[i-1] == ans[i] and ans[i] == 1):
#             cnt += 1
#             sum += cnt
#             continue
#         sum += 1
#         cnt = 1

# print(sum)


n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0

for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)
