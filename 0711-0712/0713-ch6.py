import sys
import random as r
sys.stdin = open("0711-0712/input4.txt", "rt")  # 파일 읽어오기

'''
자릿수의 합
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
각 자연수의 자릿수의 합을 구하는 def digit_sum(x)를 작성해야 함

3
125 15232 97
'''
n = int(input())
c = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x//10
    return sum


max = -2147000000

for i in c:
    tot = digit_sum(i)
    if (tot > max):
        max = tot
        res = i

print(i)

'''
다른 방법
def digit_sum(x):
  sum=0
  for i in str(x):
    sum += int(i)
  return sum
'''
