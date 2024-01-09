# 후위표기법
stk = []
n = int(input())
expression = input().split()

for n1 in expression:
    if n1 == '+':
        a = stk.pop()
        b = stk.pop()
        stk.append(b + a)
    elif n1 == '-':
        a = stk.pop()
        b = stk.pop()
        stk.append(b - a)
    elif n1 == '*':
        a = stk.pop()
        b = stk.pop()
        stk.append(b * a)
    elif n1 == '/':
        a = stk.pop()
        b = stk.pop()
        stk.append(int(b / a))
    else:
        stk.append(int(n1))

print(stk.pop())
