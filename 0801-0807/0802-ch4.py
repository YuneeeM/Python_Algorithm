import sys
import random as r
sys.stdin = open("0801/input4.txt", "rt")  # 파일 읽어오기

'''
후위식 연산

후위연산식이 주어지면 연산한 결과를 출력하는 프로그램

'''

s = input()
stack = []
sum = 0

for x in s:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            a = stack.pop()
            b = stack.pop()
            sum = b+a
            stack.append(sum)
        elif x == '-':
            a = stack.pop()
            b = stack.pop()
            sum = b-a
            stack.append(sum)
        elif x == '*':
            a = stack.pop()
            b = stack.pop()
            sum = b*a
            stack.append(sum)
        else:
            a = stack.pop()
            b = stack.pop()
            sum = b/a
            stack.append(sum)

print(stack[0])
