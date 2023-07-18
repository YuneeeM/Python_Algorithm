import sys
import random as r
sys.stdin = open("0715/input2.txt", "rt")  # 파일 읽어오기

'''
숫자만 출력
문자와 숫자가 섞여 있는 문자열 그 중 숫자만 추출하여 자연수를 만듦
그 자연수의 약수 개수를 출력
'''

s = input()
res = 0

for x in s:
    if x.isdecimal():
        res = res*10+int(x)
print(res)

cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)


# 내코드
# for i in s:
#     if i >= '0' and i <= '9':
#         res += i

# res = int(res)

# for i in range(1, res+1):
#     if res % i == 0:
#         cnt += 1


# print(res, cnt)
