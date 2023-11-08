import sys
import random as r
sys.stdin = open("0801/input2.txt", "rt")  # 파일 읽어오기

'''
쇠 막대기
여러개의 쇠막대기를 레이저로 절단하려고 한다. 효율적인 작업을 위해서 쇠막기를 아래서 위로 겹쳐 놓고,
레이저를 위에서 수직으로 발사하여 쇠막대기들을 자름


쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점을 겹치지 않도록 놓는다.
각 쇠 막대기를 자르는 레이저는 적어도 하나 존재함
레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않음

()이 완전한 쌍으로 레이지를 표현
'''
s = input()
stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
