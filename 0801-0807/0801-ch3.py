import sys
import random as r
sys.stdin = open("0801/input3.txt", "rt")  # 파일 읽어오기

'''
후위 표기식 만들기
중위 표기식이 입력되면 후위 표현식으로 변환하는 프로그램
'''

s = input()
stack = []
res = ''
for x in s:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()

print(res)
