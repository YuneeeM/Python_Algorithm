import sys
import random as r
sys.stdin = open("0801/input1.txt", "rt")  # 파일 읽어오기

'''
가장 큰 수
선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여
가장 큰 수를 만들라고 함 (단, 숫자의 순서는 유지해야 함)
5276823에서 3개의 자릿수를 제거하면
7823


스택(LIFO)
후입선출 - list를 이용해 append와 pop를 사용
'''
num, m = map(int, input().split())

num = list(map(int, str(num)))

stack = []
for x in num:
    # stack 의 의미 : stack이 null이 아니라면 참
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)
